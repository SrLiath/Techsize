# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WvfACs.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(925, 672)
        Form.setStyleSheet("background-color: rgb(234, 237, 241);")
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.frame = QFrame(Form)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet(
            "QWidget {\n"
            "	background-color: rgb(255, 255, 255);\n"
            "	border-radius: 10px;\n"
            "	border: 2px solid rgb(192, 191, 188)\n"
            "}\n"
            "\n"
            "QFrame {\n"
            "	border: 2px solid rgb(192, 191, 188)\n"
            "}"
        )
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(40, 40, 40, 40)
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName("label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies(["Segoe UI"])
        font.setPointSize(13)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(
            "QLabel {\n" "	color: black;\n" "border: none;\n" "}"
        )

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.down_1 = QFrame(self.frame)
        self.down_1.setObjectName("down_1")
        self.down_1.setMaximumSize(QSize(16777215, 100))
        self.down_1.setStyleSheet(
            "QFrame {\n"
            "border:none\n"
            "}\n"
            "\n"
            "QFrame:hover {\n"
            "	background-color: rgb(222, 221, 218)\n"
            "}"
        )
        self.down_1.setFrameShape(QFrame.StyledPanel)
        self.down_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.down_1)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.img_1 = QPushButton(self.down_1)
        self.img_1.setObjectName("img_1")
        self.img_1.setMinimumSize(QSize(150, 100))
        self.img_1.setMaximumSize(QSize(150, 100))
        self.img_1.setStyleSheet(
            "QPushButton {\n" "	border: none;\n" "	background: none;\n" "}"
        )

        self.horizontalLayout.addWidget(self.img_1)

        self.link_1 = QLabel(self.down_1)
        self.link_1.setObjectName("link_1")
        self.link_1.setMinimumSize(QSize(70, 75))
        self.link_1.setMaximumSize(QSize(25, 75))
        font1 = QFont()
        font1.setFamilies(["Segoe UI"])
        font1.setPointSize(12)
        self.link_1.setFont(font1)
        self.link_1.setStyleSheet(
            "QLabel {\n"
            "	color: black;\n"
            "	border: none;\n"
            "	padding: 5px;\n"
            "background-color: none;\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.link_1)

        self.gridLayout.addWidget(self.down_1, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.verticalLayout_3.addWidget(self.frame)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.label.setText(
            QCoreApplication.translate("Form", "Softwares:", None)
        )
        self.img_1.setText("")
        self.link_1.setText("")

    # retranslateUi
