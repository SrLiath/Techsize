# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nIlirm.ui'
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
    QLabel,
    QPlainTextEdit,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(627, 150)
        Form.setStyleSheet("background-color: rgb(234, 237, 241);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(Form)
        self.frame_6.setObjectName("frame_6")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_6.sizePolicy().hasHeightForWidth()
        )
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QSize(0, 150))
        self.frame_6.setStyleSheet("border:none;\n" "background: none")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName("frame_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.frame_8.sizePolicy().hasHeightForWidth()
        )
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setMinimumSize(QSize(400, 0))
        self.frame_8.setMaximumSize(QSize(700, 16777215))
        self.frame_8.setStyleSheet(
            "QFrame {\n"
            "	background-color: rgb(203, 245, 212);\n"
            "	border: 1px solid rgb(38, 162, 105);\n"
            "	border-radius: 5px;\n"
            "	color: black;\n"
            "}\n"
            "\n"
            "QLabel{\n"
            "	border:none\n"
            "}"
        )
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lb_criado = QLabel(self.frame_8)
        self.lb_criado.setObjectName("lb_criado")
        self.lb_criado.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(8)
        self.lb_criado.setFont(font)
        self.lb_criado.setStyleSheet("")

        self.verticalLayout_2.addWidget(self.lb_criado)

        self.plainTextEdit = QPlainTextEdit(self.frame_8)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setStyleSheet(
            "margin-top: 10px;\n"
            "border-radius: 0px;\n"
            "border: none;\n"
            "border-top: 1px solid rgb(38, 162, 105);"
        )

        self.verticalLayout_2.addWidget(self.plainTextEdit)

        self.gridLayout.addWidget(self.frame_8, 0, 1, 2, 1)

        self.lb_user = QLabel(self.frame_6)
        self.lb_user.setObjectName("lb_user")
        self.lb_user.setMinimumSize(QSize(45, 40))
        self.lb_user.setMaximumSize(QSize(45, 45))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.lb_user.setFont(font1)
        self.lb_user.setStyleSheet(
            "QLabel{\n"
            "	background: rgb(244, 143, 10);\n"
            "	border-radius: 10px;\n"
            "	color: white;\n"
            "}"
        )
        self.lb_user.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_user, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.verticalLayout.addWidget(self.frame_6)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.lb_criado.setText(
            QCoreApplication.translate("Form", "Criado em: 12/12/2022", None)
        )
        self.lb_user.setText(QCoreApplication.translate("Form", "GF", None))

    # retranslateUi
