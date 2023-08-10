# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chamado-detalhesqBGjQH.ui'
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
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(1146, 775)
        Form.setStyleSheet("background-color: rgb(234, 237, 241);")
        self.horizontalLayout_4 = QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(40, 40, 40, 40)
        self.widget = QWidget(Form)
        self.widget.setObjectName("widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.widget.sizePolicy().hasHeightForWidth()
        )
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(
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
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 4, 4, 4)
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName("frame_2")
        sizePolicy.setHeightForWidth(
            self.frame_2.sizePolicy().hasHeightForWidth()
        )
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(
            "QFrame{\n"
            "	border:none;\n"
            "	border-radius: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "	color: black;\n"
            "	border: none;\n"
            "}"
        )
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(25, 30, 25, 30)
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet("border: none")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 552, 627))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setMinimumSize(QSize(450, 0))
        self.frame_3.setStyleSheet(
            "QFrame{\n"
            "	border:none;\n"
            "	border-radius: 0px;\n"
            "	\n"
            "	background-color: rgb(222, 221, 218);\n"
            "border-left: 1px solid rgb(11, 54, 106)\n"
            "\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "	color: black;\n"
            "	border: none;\n"
            "}"
        )
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(25, 30, 25, 30)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName("label")
        self.label.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_3.addWidget(self.label)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName("frame_5")
        self.frame_5.setStyleSheet(
            "QFrame{\n"
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
            "}"
        )
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 40, -1, -1)
        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.setMinimumSize(QSize(0, 40))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName("label_8")
        self.label_8.setMinimumSize(QSize(150, 0))
        self.label_8.setMaximumSize(QSize(150, 25))
        self.label_8.setStyleSheet("QLabel {\n" "	color: black;\n" "}")
        self.label_8.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.horizontalLayout_5.addWidget(self.label_8)

        self.comboBox_3 = QComboBox(self.frame_4)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(0, 30))
        self.comboBox_3.setMaximumSize(QSize(16777215, 30))
        self.comboBox_3.setStyleSheet("")

        self.horizontalLayout_5.addWidget(self.comboBox_3)

        self.verticalLayout_4.addWidget(self.frame_4)

        self.frame_21 = QFrame(self.frame_5)
        self.frame_21.setObjectName("frame_21")
        self.frame_21.setMinimumSize(QSize(0, 40))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_42 = QLabel(self.frame_21)
        self.label_42.setObjectName("label_42")
        self.label_42.setMinimumSize(QSize(150, 0))
        self.label_42.setMaximumSize(QSize(150, 25))
        self.label_42.setStyleSheet("QLabel {\n" "	color: black;\n" "}")
        self.label_42.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.horizontalLayout_7.addWidget(self.label_42)

        self.comboBox_5 = QComboBox(self.frame_21)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.setMinimumSize(QSize(0, 30))
        self.comboBox_5.setMaximumSize(QSize(16777215, 30))
        self.comboBox_5.setStyleSheet("")

        self.horizontalLayout_7.addWidget(self.comboBox_5)

        self.verticalLayout_4.addWidget(self.frame_21)

        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName("frame")
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.label_6.setMinimumSize(QSize(150, 0))
        self.label_6.setMaximumSize(QSize(150, 25))
        self.label_6.setStyleSheet("QLabel {\n" "	color: black;\n" "}")
        self.label_6.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.horizontalLayout.addWidget(self.label_6)

        self.comboBox_2 = QComboBox(self.frame)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(0, 30))
        self.comboBox_2.setMaximumSize(QSize(16777215, 30))
        self.comboBox_2.setStyleSheet("")

        self.horizontalLayout.addWidget(self.comboBox_2)

        self.verticalLayout_4.addWidget(self.frame)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName("frame_7")
        self.frame_7.setMinimumSize(QSize(0, 40))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName("label_9")
        self.label_9.setMinimumSize(QSize(150, 0))
        self.label_9.setMaximumSize(QSize(150, 25))
        self.label_9.setStyleSheet("QLabel {\n" "	color: black;\n" "}")
        self.label_9.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.horizontalLayout_6.addWidget(self.label_9)

        self.comboBox_4 = QComboBox(self.frame_7)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(0, 30))
        self.comboBox_4.setMaximumSize(QSize(16777215, 30))
        self.comboBox_4.setStyleSheet("")

        self.horizontalLayout_6.addWidget(self.comboBox_4)

        self.verticalLayout_4.addWidget(self.frame_7)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName("label_2")
        self.label_2.setMaximumSize(QSize(16777215, 25))
        self.label_2.setFont(font)

        self.verticalLayout_4.addWidget(self.label_2)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.verticalLayout_3.addWidget(self.frame_5)

        self.horizontalLayout_2.addWidget(self.frame_3)

        self.horizontalLayout_4.addWidget(self.widget)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.label.setText(QCoreApplication.translate("Form", "Chamado", None))
        self.label_8.setText(
            QCoreApplication.translate("Form", "Data Abertura", None)
        )
        self.label_42.setText(
            QCoreApplication.translate(
                "Form", "Ultima Atualiza\u00e7\u00e3o", None
            )
        )
        self.label_6.setText(
            QCoreApplication.translate("Form", "Categoria", None)
        )
        self.label_9.setText(
            QCoreApplication.translate("Form", "Status", None)
        )
        self.label_2.setText("")

    # retranslateUi
