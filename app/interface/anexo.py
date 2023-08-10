# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'anexoSRYMhZ.ui'
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
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QWidget,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(400, 30)
        Form.setMinimumSize(QSize(0, 30))
        Form.setMaximumSize(QSize(16777215, 30))
        Form.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(Form)
        self.frame_6.setObjectName("frame_6")
        self.frame_6.setMinimumSize(QSize(0, 30))
        self.frame_6.setMaximumSize(QSize(16777215, 30))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName("label_7")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(13, 105, 63)")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setMinimumSize(QSize(30, 30))
        self.pushButton.setMaximumSize(QSize(30, 30))
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(
            "QPushButton {\n"
            "	border: none;\n"
            "	background-color: none;\n"
            "	color: black;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "	font-size: 13px\n"
            "}"
        )

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.horizontalLayout.addWidget(self.frame_6)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.label_7.setText(
            QCoreApplication.translate(
                "Form", "DANFE ITAUNA 17-12.pdf 61.08 KB (61.08Kio) ", None
            )
        )
        self.pushButton.setText(QCoreApplication.translate("Form", "X", None))

    # retranslateUi
