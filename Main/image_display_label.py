from new_models import *

import sys
from enum import Enum, auto
from typing import override
from pathlib import Path

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg


class LabelMode(Enum):

    HUMAN = auto()
    OBJECT = auto()


class ImageDisplayLabel(qtw.QLabel):

    _BOX_HUMAN_COLOR = qtc.Qt.blue
    _BOX_OBJECT_COLOR = qtc.Qt.green
    _BOX_CURRENT_COLOR = qtc.Qt.red
    _BOX_WIDTH = 2

    bboxHumanUpdated = qtc.Signal(Bbox)
    bboxObjectUpdated = qtc.Signal(Bbox)

    def __init__(self) -> None:
        super().__init__()
        self._image = None
        self._rectHuman = None
        self._rectObject = None
        self._rectCurrent = None
        self._startPoint = None
        self._endPoint = None
        self._labelMode = LabelMode.HUMAN

        self.setMouseTracking(True)
        self._mousePos = None

    @property
    def image(self) -> qtg.QPixmap | None:
        return self._image

    @image.setter
    def image(self, image: qtg.QPixmap) -> None:
        self._image = image
        self.setPixmap(image)

    def setImage(self, filename: str | Path) -> None:
        self.image = qtg.QPixmap(str(filename))
        self.resizeToFit()

    @property
    def labelMode(self) -> LabelMode:
        return self._labelMode

    @labelMode.setter
    def labelMode(self, mode: LabelMode) -> None:
        self._labelMode = mode

    @property
    def coordsHuman(self) -> Bbox | None:
        """Returns the relative coordinates."""
        if self._rectHuman is None:
            return None
        
        widget_w = self.size().width()
        widget_h = self.size().height()
        x0, y0, x1, y1 = self._rectHuman.getCoords()

        # (x0, y0) and (x1, y1) must be diagonal, but not necessarily top-left & bottom-right.
        # We convert them ourselves.

        cx = (x0 + x1) / 2
        cy = (y0 + y1) / 2
        w = abs(x0 - x1)
        h = abs(y0 - y1)

        x0 = (cx - (w / 2)) / widget_w
        y0 = (cy - (h / 2)) / widget_h
        x1 = (cx + (w / 2)) / widget_w
        y1 = (cy + (h / 2)) / widget_h

        return Bbox(x0=x0, y0=y0, x1=x1, y1=y1)

    @property
    def coordsObject(self) -> Bbox | None:
        """Returns the relative coordinates."""
        if self._rectObject is None:
            return None
        
        widget_w = self.size().width()
        widget_h = self.size().height()
        x0, y0, x1, y1 = self._rectObject.getCoords()

        # (x0, y0) and (x1, y1) must be diagonal, but not necessarily top-left & bottom-right.
        # We convert them ourselves.

        cx = (x0 + x1) / 2
        cy = (y0 + y1) / 2
        w = abs(x0 - x1)
        h = abs(y0 - y1)

        x0 = (cx - (w / 2)) / widget_w
        y0 = (cy - (h / 2)) / widget_h
        x1 = (cx + (w / 2)) / widget_w
        y1 = (cy + (h / 2)) / widget_h

        return Bbox(x0=x0, y0=y0, x1=x1, y1=y1)

    def setBboxHuman(self, bbox: Bbox | None) -> None:
        if bbox is None:
            self._rectHuman = None
            self.update()
            return

        widget_w = self.size().width()
        widget_h = self.size().height()

        x0 = int(bbox.x0 * widget_w)
        y0 = int(bbox.y0 * widget_h)
        x1 = int(bbox.x1 * widget_w)
        y1 = int(bbox.y1 * widget_h)
        w = x1 - x0
        h = y1 - y0
        self._rectHuman = qtc.QRect(x0, y0, w, h)

        # Redraw.
        self.update()

    def setBboxObject(self, bbox: Bbox) -> None:
        if bbox is None:
            self._rectObject = None
            self.update()
            return

        widget_w = self.size().width()
        widget_h = self.size().height()

        x0 = int(bbox.x0 * widget_w)
        y0 = int(bbox.y0 * widget_h)
        x1 = int(bbox.x1 * widget_w)
        y1 = int(bbox.y1 * widget_h)
        w = x1 - x0
        h = y1 - y0
        self._rectObject = qtc.QRect(x0, y0, w, h)

        # Redraw.
        self.update()

    def resizeToFit(self) -> None:
        if self.image is not None:
            self.image = self.image.scaled(
                self.size(), qtc.Qt.IgnoreAspectRatio, qtc.Qt.SmoothTransformation
            )
        # TODO: Resize the bounding boxes.

    def clearBbox(self) -> None:
        self._rectHuman = None
        self._rectObject = None
        self._rectCurrent = None

    @override
    def mousePressEvent(self, event: qtg.QMouseEvent) -> None:
        super().mousePressEvent(event)
        self._startPoint = event.position().toPoint()
        self._rectCurrent = qtc.QRect(self._startPoint, self._startPoint)

    @override
    def mouseMoveEvent(self, event: qtg.QMouseEvent) -> None:
        super().mouseMoveEvent(event)

        mousePos = event.position().toPoint()
        clampedX = max(0, min(mousePos.x(), self.width()))
        clampedY = max(0, min(mousePos.y(), self.height()))
        clampedPos = qtc.QPoint(clampedX, clampedY)
        self._mousePos = clampedPos

        if self._rectCurrent is not None:
            self._rectCurrent.setBottomRight(clampedPos)

        self.update()

    @override
    def mouseReleaseEvent(self, event: qtg.QMouseEvent) -> None:
        super().mouseReleaseEvent(event)
        if self._labelMode is LabelMode.HUMAN:
            self._rectHuman = self._rectCurrent
            self.bboxHumanUpdated.emit(self.coordsHuman)
        elif self._labelMode is LabelMode.OBJECT:
            self._rectObject = self._rectCurrent
            self.bboxObjectUpdated.emit(self.coordsObject)
        self._rectCurrent = None
        self.update()

    @override
    def paintEvent(self, event: qtg.QPaintEvent) -> None:
        super().paintEvent(event)

        painter = qtg.QPainter(self)

        if self._mousePos:
            crosshairPen = qtg.QPen(qtc.Qt.black, 1, qtc.Qt.DotLine)
            painter.setPen(crosshairPen)
            painter.drawLine(0, self._mousePos.y(), self.width(), self._mousePos.y())
            painter.drawLine(self._mousePos.x(), 0, self._mousePos.x(), self.height())

        if self._rectHuman is not None:
            pen = qtg.QPen(self._BOX_HUMAN_COLOR, self._BOX_WIDTH)
            painter.setPen(pen)
            painter.drawRect(self._rectHuman)

        if self._rectObject is not None:
            pen = qtg.QPen(self._BOX_OBJECT_COLOR, self._BOX_WIDTH)
            painter.setPen(pen)
            painter.drawRect(self._rectObject)

        if self._rectCurrent is not None:
            pen = qtg.QPen(self._BOX_CURRENT_COLOR, self._BOX_WIDTH)
            painter.setPen(pen)
            painter.drawRect(self._rectCurrent)

    @override
    def resizeEvent(self, event: qtg.QResizeEvent) -> None:
        super().resizeEvent(event)
        self.resizeToFit()

    @override
    def enterEvent(self, event: qtg.QEnterEvent) -> None:
        super().enterEvent(event)
        self._mousePos = event.position().toPoint()

    @override
    def leaveEvent(self, event: qtc.QEvent) -> None:
        super().leaveEvent(event)
        self._mousePos = None
        self.update()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = ImageDisplayLabel()
    window.show()

    sys.exit(app.exec())
