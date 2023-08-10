# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chamado-chatWilfOP.ui'
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
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(400, 200)
        Form.setStyleSheet("background-color: rgb(234, 237, 241);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(Form)
        self.frame_6.setObjectName("frame_6")
        self.frame_6.setMinimumSize(QSize(0, 200))
        self.frame_6.setMaximumSize(QSize(16777215, 200))
        self.frame_6.setStyleSheet("border:none")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName("frame_8")
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

        self.lb_titulo = QLabel(self.frame_8)
        self.lb_titulo.setObjectName("lb_titulo")
        self.lb_titulo.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.lb_titulo.setFont(font1)
        self.lb_titulo.setStyleSheet(
            "QLabel{\n"
            "	border-bottom: 1px solid rgb(38, 162, 105);\n"
            "	border-radius: none\n"
            "}"
        )
        self.lb_titulo.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )

        self.verticalLayout_2.addWidget(self.lb_titulo)

        self.lb_descricao = QLabel(self.frame_8)
        self.lb_descricao.setObjectName("lb_descricao")
        font2 = QFont()
        font2.setPointSize(10)
        self.lb_descricao.setFont(font2)

        self.verticalLayout_2.addWidget(self.lb_descricao)

        self.gridLayout.addWidget(self.frame_8, 0, 1, 2, 1)

        self.lb_user = QLabel(self.frame_6)
        self.lb_user.setObjectName("lb_user")
        self.lb_user.setMinimumSize(QSize(40, 40))
        self.lb_user.setMaximumSize(QSize(45, 45))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.lb_user.setFont(font3)
        self.lb_user.setStyleSheet(
            "QLabel{\n"
            "	background: rgb(244, 143, 10);\n"
            "	border-radius: 10px;\n"
            "	color: white;\n"
            "}"
        )
        self.lb_user.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_user, 0, 0, 1, 1)

        self.verticalLayout.addWidget(self.frame_6)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.lb_criado.setText(
            QCoreApplication.translate("Form", "Criado em: 12/12/2022", None)
        )
        self.lb_titulo.setText(
            QCoreApplication.translate("Form", "TITULO CHAMADO", None)
        )
        self.lb_descricao.setText(
            QCoreApplication.translate("Form", "Mensagem do chamado", None)
        )
        self.lb_user.setText(QCoreApplication.translate("Form", "GF", None))

    # retranslateUi
