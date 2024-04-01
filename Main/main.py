import sys
from pathlib import Path
from typing import override

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Ui.main_window import Ui_MainWindow
from image_display_label import ImageDisplayLabel, LabelMode
from models import *
from nav_list import NavList


class MainWindow(qtw.QMainWindow, Ui_MainWindow):

    statusbarMsg = "[ {} / {} ]     {}"
    imageChange = qtc.Signal()

    objectClasses = [
        "bicycle",
        "elephant",
        "horse",
        "motorcycle",
    ]

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.datasetAnnotations: list[Annotation] = []

        self.imageFolder = None
        self.imageFilepaths = None
        self.imagePointer = 0
        self.imageChange.connect(self.onImageChange)

        self.bboxList = NavList()
        self.bboxList.modified.connect(self.onBboxListModified)

        self.openAction.triggered.connect(self.onOpenActionTriggered)
        self.saveAsAction.triggered.connect(self.onSaveAsActionTriggered)
        self.closeAction.triggered.connect(self.close)

        self.humanModeButton.clicked.connect(self.onHumanModeButtonClicked)
        self.objectModeButton.clicked.connect(self.onObjectModeButtonClicked)

        self.imageLabel.bboxHumanUpdated.connect(self.onBboxHumanUpdated)
        self.imageLabel.bboxObjectUpdated.connect(self.onBboxObjectUpdated)

        self.deleteButton.clicked.connect(self.onDeleteButtonClicked)
        self.previousButton.clicked.connect(self.onPreviousButtonClicked)
        self.nextButton.clicked.connect(self.onNextButtonClicked)
        self.deleteButton.setEnabled(False)
        self.previousButton.setEnabled(False)
        self.nextButton.setEnabled(False)

        self.submitInstanceButton.clicked.connect(self.onSubmitInstanceButtonClicked)
        self.nextImageButton.clicked.connect(self.onNextImageButtonClicked)

    @qtc.Slot()
    def onImageChange(self) -> None:
        self.imagePointer += 1
        self.imageLabel.setImage(filename=self.imageFilepaths[self.imagePointer])
        self.statusbar.showMessage(
            self.statusbarMsg.format(
                self.imagePointer,
                len(self.imageFilepaths),
                self.imageFilepaths[self.imagePointer].name,
            )
        )

    @qtc.Slot()
    def onBboxListModified(self) -> None:
        boxes = self.bboxList.getCurrent()
        if boxes is None:
            self.imageLabel.setBboxHuman(None)
            self.imageLabel.setBboxObject(None)
        else:
            bboxHuman, bboxObject = boxes
            self.imageLabel.setBboxHuman(bboxHuman)
            self.imageLabel.setBboxObject(bboxObject)
        self.imageLabel.update()

        self.previousButton.setEnabled(not self.bboxList.isAtFirst())
        self.deleteButton.setEnabled(not self.bboxList.isAtNew())
        self.nextButton.setEnabled(not self.bboxList.isAtNew())

    @qtc.Slot()
    def onOpenActionTriggered(self) -> None:
        filename, _ = qtw.QFileDialog.getOpenFileName(
            parent=self,
            caption="Open Image",
            dir=None,
            filter="Image Files (*.png *.jpg)",
        )

        selectedImageFilepath = Path(filename)

        # Hack implementation to get the list of filenames after the one selected.
        # TODO: Replace with a better approach.
        imageFilepaths = sorted(selectedImageFilepath.parent.glob("*"))
        for idx, path in enumerate(imageFilepaths):
            if path.samefile(selectedImageFilepath):
                break
        self.imageFilepaths = imageFilepaths[idx:]

        # Pointer always points to the current image. -1 because image not set.
        # TODO: Improve this design.
        self.imagePointer = -1

        self.imageChange.emit()

    @qtc.Slot()
    def onSaveAsActionTriggered(self) -> None:
        filename, _ = qtw.QFileDialog.getSaveFileName(
            parent=self,
            caption="Save File",
            dir=None,
            filter="JSON file (*.json)",
        )

        dataset = Dataset(annotations=self.datasetAnnotations)

        with Path(filename).open(mode="w") as fp:
            json = dataset.model_dump_json()
            fp.write(json)

    @qtc.Slot()
    def onHumanModeButtonClicked(self) -> None:
        self.imageLabel.labelMode = LabelMode.HUMAN

    @qtc.Slot()
    def onObjectModeButtonClicked(self) -> None:
        self.imageLabel.labelMode = LabelMode.OBJECT

    @qtc.Slot()
    def onDeleteButtonClicked(self) -> None:
        self.bboxList.removeCurrent()

    @qtc.Slot()
    def onPreviousButtonClicked(self) -> None:
        self.bboxList.pointerBackward()

    @qtc.Slot()
    def onNextButtonClicked(self) -> None:
        self.bboxList.pointerForward()

    def getCaptionFull(self) -> str:
        return self.hoiEdit.toPlainText()

    def getCaptionMasked(self) -> list[str]:
        textEdits = [
            self.hoEdit,
            self.hiEdit,
            self.oiEdit,
            self.hEdit,
            self.oEdit,
            self.iEdit,
        ]
        return [te.toPlainText() for te in textEdits]

    def getCaptionAll(self) -> list[str]:
        return [self.getCaptionFull(), *self.getCaptionMasked()]

    @qtc.Slot()
    def onSubmitInstanceButtonClicked(self) -> None:
        # TODO: Save current caption annotation.
        bboxHuman, bboxObject = self.bboxList.toBboxLists()

        self.datasetAnnotations.append(
            Annotation(
                image_filename=self.imageFilepaths[self.imagePointer].name,
                object_id=self.objectClassBox.currentIndex(),
                caption_all=self.getCaptionAll(),
                caption_full=self.getCaptionFull(),
                caption_masked=self.getCaptionMasked(),
                bbox_human=bboxHuman,
                bbox_object=bboxObject,
            )
        )

        self.imageLabel.clearBbox()
        self.bboxList.clear()

        textEdits = [
            self.hoiEdit,
            self.hoEdit,
            self.hiEdit,
            self.oiEdit,
            self.hEdit,
            self.oEdit,
            self.iEdit,
        ]
        for te in textEdits:
            te.clear()

    @qtc.Slot()
    def onNextImageButtonClicked(self) -> None:
        self.imageChange.emit()
        self.imageLabel.clearBbox()
        self.bboxList.clear()

        textEdits = [
            self.hoiEdit,
            self.hoEdit,
            self.hiEdit,
            self.oiEdit,
            self.hEdit,
            self.oEdit,
            self.iEdit,
        ]
        for te in textEdits:
            te.clear()

    @qtc.Slot(Bbox)
    def onBboxHumanUpdated(self, bbox: Bbox) -> None:
        # TODO: Fix hack implementation.
        currentBoxes = self.bboxList.getCurrent()
        try:
            _, bboxObject = currentBoxes
            newBoxes = (bbox, bboxObject)
        except TypeError:
            newBoxes = (bbox, None)
        self.bboxList.setCurrent(newBoxes)

    @qtc.Slot(Bbox)
    def onBboxObjectUpdated(self, bbox: Bbox) -> None:
        # TODO: Fix hack implementation.
        currentBoxes = self.bboxList.getCurrent()
        try:
            bboxHuman, _ = currentBoxes
            newBoxes = (bboxHuman, bbox)
        except TypeError:
            newBoxes = (None, bbox)
        self.bboxList.setCurrent(newBoxes)

    @override
    def setupUi(self, mainWindow: qtw.QMainWindow) -> None:
        """
        Hack to replace the placeholder label with custom label that allows drawing.
        # TODO: Find a better approach that does this in Qt Designer (promote to class?).
        """
        super().setupUi(mainWindow)

        # Remove the placeholder label.
        placeholder_item = self.labellerHLayout.takeAt(self.labellerHLayout.count() - 1)
        placeholder_widget = placeholder_item.widget()
        if placeholder_widget is not None:
            placeholder_widget.deleteLater()

        self.imageLabel = ImageDisplayLabel()
        self.labellerHLayout.addWidget(self.imageLabel)
        self.labellerHLayout.setStretch(2, 9)

        # TODO: Fix hardcoding.
        self.objectClassBox.addItems(self.objectClasses)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
