# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BFHFJU.ui'
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
    QTimer,
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
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(500, 500)
        Form.setMinimumSize(QSize(500, 500))
        Form.setMaximumSize(QSize(500, 500))
        Form.setStyleSheet("background-color: rgb(234, 237, 241);")
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(100, 32, 100, -1)
        self.logo = QPushButton(Form)
        self.logo.setObjectName("logo")
        self.logo.setMinimumSize(QSize(0, 150))
        self.logo.setMaximumSize(QSize(16777215, 150))
        font = QFont()
        font.setBold(True)
        self.logo.setFont(font)
        self.logo.setStyleSheet(
            "QPushButton{\n"
            "	border: none;\n"
            "	background-color: none;\n"
            "}"
        )
        self.logo.setIconSize(QSize(245, 169))

        self.verticalLayout_3.addWidget(self.logo)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.label_3.setMaximumSize(QSize(16777215, 0))
        self.label_3.setStyleSheet(
            "QLabel {\n"
            "	color: white;\n"
            "	background-color: rgb(237, 51, 59);\n"
            "	text-align: center;\n"
            "	border-radius: 10px;\n"
            "}"
        )
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.widget = QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: black;")

        self.verticalLayout.addWidget(self.label)

        self.input_tokenAPI = QLineEdit(self.widget)
        self.input_tokenAPI.setObjectName("input_tokenAPI")
        self.input_tokenAPI.setStyleSheet("color: black;")

        self.verticalLayout.addWidget(self.input_tokenAPI)

        self.verticalLayout_3.addWidget(self.widget)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color: black;")

        self.verticalLayout_2.addWidget(self.label_2)

        self.input_tokenUser = QLineEdit(self.widget_2)
        self.input_tokenUser.setObjectName("input_tokenUser")
        self.input_tokenUser.setStyleSheet("color: black;")

        self.verticalLayout_2.addWidget(self.input_tokenUser)

        self.verticalLayout_3.addWidget(self.widget_2)

        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.widget_3)

        self.btn_cadastrar = QPushButton(Form)
        self.btn_cadastrar.setObjectName("btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setStyleSheet(
            "QPushButton {\n"
            "	background-color: rgb(43, 62, 99);\n"
            "	border: none;\n"
            "	border-radius: 5px;\n"
            "	padding: 4px;\n"
            "	color: white;\n"
            "	font-size: 12px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "	padding: 2px;\n"
            "	background: rgb(28, 41, 69);\n"
            "	color: #E6A95F;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "	background: rgb(39, 51, 76);\n"
            "}"
        )

        self.verticalLayout_3.addWidget(self.btn_cadastrar)

        # Label que indica erros
        self.error_informer_label = QLabel(Form)
        self.error_informer_label.setObjectName("error_informer_label")
        self.error_informer_label.setAlignment(Qt.AlignCenter)
        self.error_informer_label.setStyleSheet("color: red;")
        self.error_informer_label.setVisible(False)
        self.verticalLayout_3.addWidget(self.error_informer_label)
        # end

        self.widget_4 = QWidget(Form)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_5 = QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.widget_4)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def show_error_label(self) -> None:
        self.error_informer_label.setVisible(True)
        QTimer.singleShot(3000, self.hide_error_label)

    def hide_error_label(self) -> None:
        self.error_informer_label.setVisible(False)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.logo.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", "ERRRO", None))
        self.label.setText(
            QCoreApplication.translate("Form", "Token API", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("Form", "Token Usuario", None)
        )
        self.btn_cadastrar.setText(
            QCoreApplication.translate("Form", "Cadastrar", None)
        )
        # Texto do Label de erros
        self.error_informer_label.setText(
            QCoreApplication.translate("Form", "", None)
        )
        # end

    # retranslateUi
