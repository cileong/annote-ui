# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(995, 715)
        self.openAction = QAction(MainWindow)
        self.openAction.setObjectName(u"openAction")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.saveAsAction = QAction(MainWindow)
        self.saveAsAction.setObjectName(u"saveAsAction")
        self.closeAction = QAction(MainWindow)
        self.closeAction.setObjectName(u"closeAction")
        self.quitAction = QAction(MainWindow)
        self.quitAction.setObjectName(u"quitAction")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.labellerHLayout = QHBoxLayout(self.groupBox_2)
        self.labellerHLayout.setObjectName(u"labellerHLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.humanModeButton = QPushButton(self.groupBox_2)
        self.humanModeButton.setObjectName(u"humanModeButton")
        self.humanModeButton.setMinimumSize(QSize(75, 75))
        icon = QIcon(QIcon.fromTheme(u"start-here"))
        self.humanModeButton.setIcon(icon)

        self.verticalLayout_6.addWidget(self.humanModeButton)

        self.objectModeButton = QPushButton(self.groupBox_2)
        self.objectModeButton.setObjectName(u"objectModeButton")
        self.objectModeButton.setMinimumSize(QSize(75, 75))

        self.verticalLayout_6.addWidget(self.objectModeButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.labellerHLayout.addLayout(self.verticalLayout_6)

        self.line_3 = QFrame(self.groupBox_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.labellerHLayout.addWidget(self.line_3)

        self.imageLabel = QLabel(self.groupBox_2)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setAlignment(Qt.AlignCenter)

        self.labellerHLayout.addWidget(self.imageLabel)

        self.labellerHLayout.setStretch(2, 9)

        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.previousButton = QPushButton(self.centralwidget)
        self.previousButton.setObjectName(u"previousButton")
        self.previousButton.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.previousButton)

        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.deleteButton)

        self.nextButton = QPushButton(self.centralwidget)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.nextButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.objectClassBox = QComboBox(self.groupBox)
        self.objectClassBox.setObjectName(u"objectClassBox")
        self.objectClassBox.setMinimumSize(QSize(0, 30))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.objectClassBox)

        self.objectClassLabel = QLabel(self.groupBox)
        self.objectClassLabel.setObjectName(u"objectClassLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.objectClassLabel)


        self.verticalLayout.addLayout(self.formLayout)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.hoiEdit = QPlainTextEdit(self.groupBox)
        self.hoiEdit.setObjectName(u"hoiEdit")
        self.hoiEdit.setTabChangesFocus(True)
        self.hoiEdit.setBackgroundVisible(False)

        self.verticalLayout.addWidget(self.hoiEdit)

        self.hoEdit = QPlainTextEdit(self.groupBox)
        self.hoEdit.setObjectName(u"hoEdit")
        self.hoEdit.setTabChangesFocus(True)

        self.verticalLayout.addWidget(self.hoEdit)

        self.hiEdit = QPlainTextEdit(self.groupBox)
        self.hiEdit.setObjectName(u"hiEdit")
        self.hiEdit.setTabChangesFocus(True)

        self.verticalLayout.addWidget(self.hiEdit)

        self.oiEdit = QPlainTextEdit(self.groupBox)
        self.oiEdit.setObjectName(u"oiEdit")
        self.oiEdit.setTabChangesFocus(True)

        self.verticalLayout.addWidget(self.oiEdit)

        self.hEdit = QPlainTextEdit(self.groupBox)
        self.hEdit.setObjectName(u"hEdit")
        self.hEdit.setTabChangesFocus(True)

        self.verticalLayout.addWidget(self.hEdit)

        self.oEdit = QPlainTextEdit(self.groupBox)
        self.oEdit.setObjectName(u"oEdit")
        self.oEdit.setTabChangesFocus(True)

        self.verticalLayout.addWidget(self.oEdit)

        self.iEdit = QPlainTextEdit(self.groupBox)
        self.iEdit.setObjectName(u"iEdit")
        self.iEdit.setTabChangesFocus(True)

        self.verticalLayout.addWidget(self.iEdit)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.submitInstanceButton = QPushButton(self.centralwidget)
        self.submitInstanceButton.setObjectName(u"submitInstanceButton")
        self.submitInstanceButton.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.submitInstanceButton)

        self.nextImageButton = QPushButton(self.centralwidget)
        self.nextImageButton.setObjectName(u"nextImageButton")
        self.nextImageButton.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.nextImageButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.setStretch(0, 6)
        self.horizontalLayout_2.setStretch(2, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 995, 22))
        self.fileMenu = QMenu(self.menubar)
        self.fileMenu.setObjectName(u"fileMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.objectClassBox, self.hoiEdit)
        QWidget.setTabOrder(self.hoiEdit, self.hoEdit)
        QWidget.setTabOrder(self.hoEdit, self.hiEdit)
        QWidget.setTabOrder(self.hiEdit, self.oiEdit)
        QWidget.setTabOrder(self.oiEdit, self.hEdit)
        QWidget.setTabOrder(self.hEdit, self.oEdit)
        QWidget.setTabOrder(self.oEdit, self.iEdit)
        QWidget.setTabOrder(self.iEdit, self.humanModeButton)
        QWidget.setTabOrder(self.humanModeButton, self.objectModeButton)
        QWidget.setTabOrder(self.objectModeButton, self.previousButton)
        QWidget.setTabOrder(self.previousButton, self.deleteButton)
        QWidget.setTabOrder(self.deleteButton, self.nextButton)
        QWidget.setTabOrder(self.nextButton, self.submitInstanceButton)

        self.menubar.addAction(self.fileMenu.menuAction())
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.saveAsAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.closeAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.quitAction)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"HOIDTC Annotation Tool", None))
        self.openAction.setText(QCoreApplication.translate("MainWindow", u"&Open...", None))
#if QT_CONFIG(shortcut)
        self.openAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.saveAsAction.setText(QCoreApplication.translate("MainWindow", u"Save &As...", None))
#if QT_CONFIG(shortcut)
        self.saveAsAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.closeAction.setText(QCoreApplication.translate("MainWindow", u"&Close", None))
#if QT_CONFIG(shortcut)
        self.closeAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F4", None))
#endif // QT_CONFIG(shortcut)
        self.quitAction.setText(QCoreApplication.translate("MainWindow", u"&Quit", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Bounding box", None))
        self.humanModeButton.setText(QCoreApplication.translate("MainWindow", u"Human", None))
        self.objectModeButton.setText(QCoreApplication.translate("MainWindow", u"Object", None))
        self.imageLabel.setText(QCoreApplication.translate("MainWindow", u"ImageLabel", None))
        self.previousButton.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Captions", None))
        self.objectClassLabel.setText(QCoreApplication.translate("MainWindow", u"Object class:", None))
        self.hoiEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"human + object + interaction", None))
        self.hoEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"human + object", None))
        self.hiEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"human + interaction", None))
        self.oiEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"object + interaction", None))
        self.hEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"human", None))
        self.oEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"object", None))
        self.iEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"interaction", None))
        self.submitInstanceButton.setText(QCoreApplication.translate("MainWindow", u"Submit instance", None))
        self.nextImageButton.setText(QCoreApplication.translate("MainWindow", u"Next image", None))
        self.fileMenu.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
    # retranslateUi

