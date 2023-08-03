# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'xdp-abrir_chamado.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(954, 550)
        Form.setMinimumSize(QSize(0, 550))
        Form.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 400))
        self.widget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(450, 0))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"background-color: rgb(44, 49, 60);\n"
"\n"
"}\n"
"\n"
"QLabel {\n"
"	color: black;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(25, 30, 25, 30)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white;\n"
"")

        self.verticalLayout.addWidget(self.label)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"\n"
"QComboBox {\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(222, 221, 218);\n"
"	color: black;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	background-color: rgb(230, 97, 0);\n"
"}\n"
"\n"
"QDateEdit {\n"
"	border-radius: 3px;\n"
"\n"
"	color: black;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"	background-color: rgb(230, 97, 0);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 30, -1, -1)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(150, 0))
        self.label_4.setMaximumSize(QSize(150, 25))
        self.label_4.setStyleSheet(u"color: white;\n"
"")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.lb_titulo = QLineEdit(self.frame_4)
        self.lb_titulo.setObjectName(u"lb_titulo")
        self.lb_titulo.setMinimumSize(QSize(0, 30))
        self.lb_titulo.setMaximumSize(QSize(500, 40))
        self.lb_titulo.setStyleSheet(u"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"color:white;")

        self.verticalLayout_2.addWidget(self.lb_titulo)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(150, 0))
        self.label_6.setMaximumSize(QSize(150, 25))
        self.label_6.setStyleSheet(u"color: white;\n"
"")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_6)

        self.lineEdit_nome = QLineEdit(self.frame_4)
        self.lineEdit_nome.setObjectName(u"lineEdit_nome")
        self.lineEdit_nome.setMinimumSize(QSize(0, 30))
        self.lineEdit_nome.setMaximumSize(QSize(500, 40))
        self.lineEdit_nome.setStyleSheet(u"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"color:white;")

        self.verticalLayout_2.addWidget(self.lineEdit_nome)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(150, 0))
        self.label_5.setMaximumSize(QSize(150, 25))
        self.label_5.setStyleSheet(u"color: white;\n"
"")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_5)

        self.txt_descricao = QPlainTextEdit(self.frame_4)
        self.txt_descricao.setObjectName(u"txt_descricao")
        self.txt_descricao.setMinimumSize(QSize(0, 200))
        self.txt_descricao.setMaximumSize(QSize(16777215, 400))
        self.txt_descricao.setStyleSheet(u"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"color:white;")

        self.verticalLayout_2.addWidget(self.txt_descricao)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_adicionar = QPushButton(self.frame)
        self.btn_adicionar.setObjectName(u"btn_adicionar")
        self.btn_adicionar.setMinimumSize(QSize(0, 35))
        self.btn_adicionar.setMaximumSize(QSize(300, 35))
        font1 = QFont()
        font1.setBold(True)
        self.btn_adicionar.setFont(font1)
        self.btn_adicionar.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"color: white;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_adicionar)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_4, 0, Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(450, 1))
        self.frame_3.setMaximumSize(QSize(450, 16777215))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"	border-radius: 0px;\n"
"	\n"
"background-color: rgb(57, 65, 80);\n"
"border-left: 1px solid rgb(11, 54, 106)\n"
"\n"
"}\n"
"\n"
"QLabel {\n"
"	color: black;\n"
"	border: none;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(25, 30, 25, 30)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"	border-left: none;\n"
"	border-radius: 0px;\n"
"	border: none;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QComboBox {\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(222, 221, 218);\n"
"	color: black;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	background-color: rgb(230, 97, 0);\n"
"}\n"
"\n"
"QDateEdit {\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(222, 221, 218);\n"
"	color: black;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"	background-color: rgb(230, 97, 0);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 25, -1, -1)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 25))
        self.label_2.setFont(font)

        self.verticalLayout_4.addWidget(self.label_2)

        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 50))
        self.frame_12.setMaximumSize(QSize(16777215, 50))
        self.frame_12.setStyleSheet(u"QFrame{\n"
"	border-left: none;\n"
"	border-radius: 0px;\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setSpacing(15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(150, 0))
        self.label_11.setMaximumSize(QSize(150, 25))
        self.label_11.setStyleSheet(u"color: white;\n"
"")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_11)

        self.cb_categoria = QComboBox(self.frame_12)
        self.cb_categoria.setObjectName(u"cb_categoria")
        self.cb_categoria.setMinimumSize(QSize(0, 30))
        self.cb_categoria.setMaximumSize(QSize(16777215, 30))
        self.cb_categoria.setStyleSheet(u"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"color:white;")

        self.horizontalLayout_12.addWidget(self.cb_categoria)


        self.verticalLayout_4.addWidget(self.frame_12)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 50))
        self.frame_9.setMaximumSize(QSize(16777215, 50))
        self.frame_9.setStyleSheet(u"QFrame{\n"
"	border-left: none;\n"
"	border-radius: 0px;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(150, 0))
        self.label_7.setMaximumSize(QSize(150, 25))
        self.label_7.setStyleSheet(u"color: white;\n"
"")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.cb_subcategoria = QComboBox(self.frame_9)
        self.cb_subcategoria.setObjectName(u"cb_subcategoria")
        self.cb_subcategoria.setMinimumSize(QSize(0, 30))
        self.cb_subcategoria.setMaximumSize(QSize(16777215, 30))
        self.cb_subcategoria.setStyleSheet(u"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"color:white;")

        self.horizontalLayout_8.addWidget(self.cb_subcategoria)


        self.verticalLayout_4.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 50))
        self.frame_11.setMaximumSize(QSize(16777215, 50))
        self.frame_11.setStyleSheet(u"QFrame{\n"
"	border-left: none;\n"
"	border-radius: 0px;\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setSpacing(15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_11)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(150, 0))
        self.label_10.setMaximumSize(QSize(150, 25))
        self.label_10.setStyleSheet(u"color: white;\n"
"")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.cb_action_subcategoria = QComboBox(self.frame_11)
        self.cb_action_subcategoria.setObjectName(u"cb_action_subcategoria")
        self.cb_action_subcategoria.setMinimumSize(QSize(0, 30))
        self.cb_action_subcategoria.setMaximumSize(QSize(16777215, 30))
        self.cb_action_subcategoria.setStyleSheet(u"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"color:white;")

        self.horizontalLayout_11.addWidget(self.cb_action_subcategoria)


        self.verticalLayout_4.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 50))
        self.frame_10.setMaximumSize(QSize(16777215, 50))
        self.frame_10.setStyleSheet(u"QFrame{\n"
"	border-left: none;\n"
"	border-radius: 0px;\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(150, 0))
        self.label_8.setMaximumSize(QSize(150, 25))
        self.label_8.setStyleSheet(u"color: white;\n"
"")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.cb_urgencia = QComboBox(self.frame_10)
        self.cb_urgencia.setObjectName(u"cb_urgencia")
        self.cb_urgencia.setMinimumSize(QSize(0, 30))
        self.cb_urgencia.setMaximumSize(QSize(16777215, 30))
        self.cb_urgencia.setStyleSheet(u"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"color:white;")

        self.horizontalLayout_9.addWidget(self.cb_urgencia)


        self.verticalLayout_4.addWidget(self.frame_10)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_anexo = QPushButton(self.frame_6)
        self.btn_anexo.setObjectName(u"btn_anexo")
        self.btn_anexo.setMinimumSize(QSize(130, 35))
        self.btn_anexo.setMaximumSize(QSize(130, 35))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.btn_anexo.setFont(font2)
        self.btn_anexo.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"color: white;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_anexo)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setBold(False)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: white;\n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.scrollArea = QScrollArea(self.frame_5)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(100, 0))
        self.scrollArea.setStyleSheet(u"border: none;\n"
"\n"
"background-color: rgb(75, 65, 80);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 381, 117))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Chamado", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"T\u00edtulo", None))
        self.lb_titulo.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"Nome do solicitante", None))
        self.lineEdit_nome.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Descri\u00e7\u00e3o", None))
        self.btn_adicionar.setText(QCoreApplication.translate("Form", u"Adicionar", None))
        self.label_2.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"Categoria", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Subcategoria", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"A\u00e7\u00e3o da subcategoria", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Urg\u00eancia", None))
        self.btn_anexo.setText(QCoreApplication.translate("Form", u"Adicionar Anexo", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Arquivo(s) (20 MB m\u00e1x)", None))
    # retranslateUi

