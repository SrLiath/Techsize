# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'xdp-chamados.ui'
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
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1100, 569)
        Form.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout = QHBoxLayout(self.page)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 300))
        self.widget.setStyleSheet(u"QWidget {\n"
"background-color: rgb(44, 49, 60);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame {\n"
"	border: 2px solid rgb(44, 49, 60);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(100, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 0))
        self.label.setMaximumSize(QSize(100, 30))
        self.label.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	border:none;\n"
"}")

        self.horizontalLayout_2.addWidget(self.label)

        self.cb_filtro = QComboBox(self.frame)
        self.cb_filtro.addItem("")
        self.cb_filtro.addItem("")
        self.cb_filtro.addItem("")
        self.cb_filtro.addItem("")
        self.cb_filtro.addItem("")
        self.cb_filtro.addItem("")
        self.cb_filtro.setObjectName(u"cb_filtro")
        self.cb_filtro.setMinimumSize(QSize(200, 0))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        self.cb_filtro.setFont(font)
        self.cb_filtro.setAutoFillBackground(False)
        self.cb_filtro.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.cb_filtro.setIconSize(QSize(16, 16))
        self.cb_filtro.setFrame(True)

        self.horizontalLayout_2.addWidget(self.cb_filtro)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_atualizar = QPushButton(self.frame)
        self.btn_atualizar.setObjectName(u"btn_atualizar")
        self.btn_atualizar.setMinimumSize(QSize(150, 50))
        self.btn_atualizar.setMaximumSize(QSize(150, 50))
        font1 = QFont()
        font1.setBold(True)
        self.btn_atualizar.setFont(font1)
        self.btn_atualizar.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"		background-color: rgb(52, 59, 72);\n"
"	border:  none;\n"
"	margin-bottom: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_atualizar)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, -1, 9, -1)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(80, 0))
        self.label_2.setMaximumSize(QSize(80, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	border: none\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 0))
        self.label_3.setMaximumSize(QSize(150, 16777215))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	border: none\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 0))
        self.label_6.setMaximumSize(QSize(100, 16777215))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	border: none\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(120, 0))
        self.label_13.setMaximumSize(QSize(120, 16777215))
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	border: none\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_13)

        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(120, 0))
        self.label_15.setMaximumSize(QSize(120, 16777215))
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	border: none\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_15)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(120, 0))
        self.label_5.setMaximumSize(QSize(120, 16777215))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	border: none\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(120, 0))
        self.label_7.setMaximumSize(QSize(120, 16777215))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	border: none\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(120, 0))
        self.label_8.setMaximumSize(QSize(120, 16777215))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	border: none\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_8)


        self.verticalLayout.addWidget(self.frame_2)

        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet(u"QWidget{\n"
"	border-radius: 0px;\n"
"	border: none\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1060, 429))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContents_2.setMinimumSize(QSize(0, 0))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"QScrollArea{\n"
"	border-radius: 0px\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.scrollArea)


        self.horizontalLayout.addWidget(self.widget)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_26 = QHBoxLayout(self.page_2)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.page_2)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.widget_2.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(192, 191, 188)\n"
"}\n"
"\n"
"QFrame {\n"
"	border: 2px solid rgb(192, 191, 188)\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 4, 4, 4)
        self.frame_3 = QFrame(self.widget_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"	border-radius: 0px;\n"
"\n"
"}\n"
"\n"
"QLabel {\n"
"	color: white;\n"
"	border: none;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 30, 25, 30)
        self.scrollArea_2 = QScrollArea(self.frame_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"border: none")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 518, 501))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_4.addWidget(self.scrollArea_2)


        self.horizontalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.widget_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(300, 0))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"	\n"
"border-left: 1px solid rgb(11, 54, 106)\n"
"\n"
"}\n"
"\n"
"QLabel {\n"
"	color: black;\n"
"	border: none;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(25, 30, 25, 30)
        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 40))
        self.frame_9.setStyleSheet(u"border:none")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_28.setSpacing(20)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 25))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_28.addWidget(self.label_4)

        self.btn_voltar = QPushButton(self.frame_9)
        self.btn_voltar.setObjectName(u"btn_voltar")
        self.btn_voltar.setMinimumSize(QSize(60, 0))
        self.btn_voltar.setMaximumSize(QSize(60, 16777215))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.btn_voltar.setFont(font4)
        self.btn_voltar.setStyleSheet(u"QPushButton {\n"
"color: rgb(98, 103, 111);\n"
"\n"
"	background-color: none;\n"
"	border-radius: 10px;\n"
"	border:  none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_28.addWidget(self.btn_voltar)


        self.verticalLayout_6.addWidget(self.frame_9)

        self.frame_5 = QFrame(self.frame_4)
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
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 18, -1, -1)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 40))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_22.setSpacing(20)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(150, 0))
        self.label_9.setMaximumSize(QSize(150, 25))
        self.label_9.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_9)

        self.input_abertura = QLineEdit(self.frame_6)
        self.input_abertura.setObjectName(u"input_abertura")
        self.input_abertura.setMinimumSize(QSize(0, 30))
        self.input_abertura.setMaximumSize(QSize(16777215, 30))
        self.input_abertura.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"color: white;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_22.addWidget(self.input_abertura)


        self.verticalLayout_7.addWidget(self.frame_6)

        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 60))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_27.setSpacing(20)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_17 = QLabel(self.frame_12)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(150, 0))
        self.label_17.setMaximumSize(QSize(150, 50))
        self.label_17.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_17.setWordWrap(True)

        self.horizontalLayout_27.addWidget(self.label_17)

        self.input_tempoAtendimento = QLineEdit(self.frame_12)
        self.input_tempoAtendimento.setObjectName(u"input_tempoAtendimento")
        self.input_tempoAtendimento.setMinimumSize(QSize(0, 30))
        self.input_tempoAtendimento.setMaximumSize(QSize(16777215, 30))
        self.input_tempoAtendimento.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"color: white;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_27.addWidget(self.input_tempoAtendimento)


        self.verticalLayout_7.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_5)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 40))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_30.setSpacing(20)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_18 = QLabel(self.frame_13)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(150, 0))
        self.label_18.setMaximumSize(QSize(150, 25))
        self.label_18.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.label_18)

        self.input_tempoSolucao = QLineEdit(self.frame_13)
        self.input_tempoSolucao.setObjectName(u"input_tempoSolucao")
        self.input_tempoSolucao.setMinimumSize(QSize(0, 30))
        self.input_tempoSolucao.setMaximumSize(QSize(16777215, 30))
        self.input_tempoSolucao.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"color: white;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_30.addWidget(self.input_tempoSolucao)


        self.verticalLayout_7.addWidget(self.frame_13)

        self.frame_21 = QFrame(self.frame_5)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 40))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_23.setSpacing(20)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_45 = QLabel(self.frame_21)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(150, 0))
        self.label_45.setMaximumSize(QSize(150, 25))
        self.label_45.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.label_45.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.label_45)

        self.input_atualizacao = QLineEdit(self.frame_21)
        self.input_atualizacao.setObjectName(u"input_atualizacao")
        self.input_atualizacao.setMinimumSize(QSize(0, 30))
        self.input_atualizacao.setMaximumSize(QSize(16777215, 30))
        self.input_atualizacao.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"color: white;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_23.addWidget(self.input_atualizacao)


        self.verticalLayout_7.addWidget(self.frame_21)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 40))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_24.setSpacing(20)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(150, 0))
        self.label_10.setMaximumSize(QSize(150, 25))
        self.label_10.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.label_10)

        self.input_categoria = QLineEdit(self.frame_7)
        self.input_categoria.setObjectName(u"input_categoria")
        self.input_categoria.setMinimumSize(QSize(0, 30))
        self.input_categoria.setMaximumSize(QSize(16777215, 30))
        self.input_categoria.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"color: white;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_24.addWidget(self.input_categoria)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 40))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_29.setSpacing(20)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_14 = QLabel(self.frame_10)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(150, 0))
        self.label_14.setMaximumSize(QSize(150, 25))
        self.label_14.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.label_14)

        self.input_urgencia_2 = QLineEdit(self.frame_10)
        self.input_urgencia_2.setObjectName(u"input_urgencia_2")
        self.input_urgencia_2.setMinimumSize(QSize(0, 30))
        self.input_urgencia_2.setMaximumSize(QSize(16777215, 30))
        self.input_urgencia_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"color: white;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_29.addWidget(self.input_urgencia_2)


        self.verticalLayout_7.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 40))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_31.setSpacing(20)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_16 = QLabel(self.frame_11)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(150, 0))
        self.label_16.setMaximumSize(QSize(150, 25))
        self.label_16.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.label_16)

        self.input_tecnico_2 = QLineEdit(self.frame_11)
        self.input_tecnico_2.setObjectName(u"input_tecnico_2")
        self.input_tecnico_2.setMinimumSize(QSize(0, 30))
        self.input_tecnico_2.setMaximumSize(QSize(16777215, 30))
        self.input_tecnico_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"color: white;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_31.addWidget(self.input_tecnico_2)


        self.verticalLayout_7.addWidget(self.frame_11)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 40))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_25.setSpacing(20)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_11 = QLabel(self.frame_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(150, 0))
        self.label_11.setMaximumSize(QSize(150, 25))
        self.label_11.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.label_11)

        self.input_status = QLineEdit(self.frame_8)
        self.input_status.setObjectName(u"input_status")
        self.input_status.setMinimumSize(QSize(0, 30))
        self.input_status.setMaximumSize(QSize(16777215, 30))
        self.input_status.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"color: white;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_25.addWidget(self.input_status)


        self.verticalLayout_7.addWidget(self.frame_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.verticalLayout_6.addWidget(self.frame_5)


        self.horizontalLayout_4.addWidget(self.frame_4)


        self.horizontalLayout_26.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"FIltro:", None))
        self.cb_filtro.setItemText(0, "")
        self.cb_filtro.setItemText(1, QCoreApplication.translate("Form", u"Em atendimento (atribu\u00eddo)", None))
        self.cb_filtro.setItemText(2, QCoreApplication.translate("Form", u"Em atendimento (planejado)", None))
        self.cb_filtro.setItemText(3, QCoreApplication.translate("Form", u"Pendente", None))
        self.cb_filtro.setItemText(4, QCoreApplication.translate("Form", u"Solucionado", None))
        self.cb_filtro.setItemText(5, QCoreApplication.translate("Form", u"Fechado", None))

        self.btn_atualizar.setText(QCoreApplication.translate("Form", u"Atualizar", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Id", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Titulo", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Status", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Tempo Atendimento", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Tempo Solu\u00e7\u00e3o", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Categoria", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Data Cria\u00e7\u00e3o", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Ultima Atualiza\u00e7\u00e3o", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Chamado", None))
        self.btn_voltar.setText(QCoreApplication.translate("Form", u"Voltar", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Data Abertura", None))
        self.input_abertura.setText("")
        self.input_abertura.setPlaceholderText("")
        self.label_17.setText(QCoreApplication.translate("Form", u"Tempo para Atendimento", None))
        self.input_tempoAtendimento.setText("")
        self.input_tempoAtendimento.setPlaceholderText("")
        self.label_18.setText(QCoreApplication.translate("Form", u"Tempo para Solu\u00e7\u00e3o", None))
        self.input_tempoSolucao.setText("")
        self.input_tempoSolucao.setPlaceholderText("")
        self.label_45.setText(QCoreApplication.translate("Form", u"Ultima Atualiza\u00e7\u00e3o", None))
        self.input_atualizacao.setText("")
        self.input_atualizacao.setPlaceholderText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"Categoria", None))
        self.input_categoria.setText("")
        self.input_categoria.setPlaceholderText("")
        self.label_14.setText(QCoreApplication.translate("Form", u"Urg\u00eancia", None))
        self.input_urgencia_2.setText("")
        self.input_urgencia_2.setPlaceholderText("")
        self.label_16.setText(QCoreApplication.translate("Form", u"T\u00e9cnico Respons\u00e1vel", None))
        self.input_tecnico_2.setText("")
        self.input_tecnico_2.setPlaceholderText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"Status", None))
        self.input_status.setText("")
        self.input_status.setPlaceholderText("")
    # retranslateUi

