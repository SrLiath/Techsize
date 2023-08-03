# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inppuL.ui'
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
    QSizePolicy,
    QWidget,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(1021, 130)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(0, 80))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.item_chamado = QFrame(Form)
        self.item_chamado.setObjectName("item_chamado")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.item_chamado.sizePolicy().hasHeightForWidth()
        )
        self.item_chamado.setSizePolicy(sizePolicy1)
        self.item_chamado.setMinimumSize(QSize(0, 50))
        self.item_chamado.setStyleSheet(
            "QFrame{\n"
            "	border-radius: 0;\n"
            "	border: none;\n"
            "	border-left: 3px solid green;\n"
            "	border-bottom: 1px solid rgb(222, 221, 218);\n"
            "	background-color: none;\n"
            "}\n"
            "\n"
            "QFrame:hover{\n"
            "	background-color: rgb(195, 215, 239);\n"
            "}"
        )
        self.item_chamado.setFrameShape(QFrame.StyledPanel)
        self.item_chamado.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.item_chamado)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lb_id = QLabel(self.item_chamado)
        self.lb_id.setObjectName("lb_id")
        self.lb_id.setMinimumSize(QSize(80, 0))
        self.lb_id.setMaximumSize(QSize(80, 16777215))
        font = QFont()
        font.setPointSize(9)
        self.lb_id.setFont(font)
        self.lb_id.setStyleSheet(
            "QLabel{\n" "	color: black;\n" "	border: none\n" "}"
        )

        self.horizontalLayout_5.addWidget(self.lb_id)

        self.lb_titulo = QLabel(self.item_chamado)
        self.lb_titulo.setObjectName("lb_titulo")
        self.lb_titulo.setMinimumSize(QSize(150, 0))
        self.lb_titulo.setMaximumSize(QSize(150, 16777215))
        self.lb_titulo.setFont(font)
        self.lb_titulo.setStyleSheet(
            "QLabel{\n" "	color: black;\n" "	border: none\n" "}"
        )
        self.lb_titulo.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.lb_titulo)

        self.lb_status = QLabel(self.item_chamado)
        self.lb_status.setObjectName("lb_status")
        self.lb_status.setMinimumSize(QSize(100, 0))
        self.lb_status.setMaximumSize(QSize(100, 16777215))
        self.lb_status.setFont(font)
        self.lb_status.setStyleSheet(
            "QLabel{\n" "	color: black;\n" "	border: none\n" "}"
        )
        self.lb_status.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.lb_status)

        self.lb_tempoAtendimento = QLabel(self.item_chamado)
        self.lb_tempoAtendimento.setObjectName("lb_tempoAtendimento")
        self.lb_tempoAtendimento.setMinimumSize(QSize(120, 0))
        self.lb_tempoAtendimento.setMaximumSize(QSize(120, 16777215))
        self.lb_tempoAtendimento.setFont(font)
        self.lb_tempoAtendimento.setStyleSheet(
            "QLabel{\n" "	color: black;\n" "	border: none\n" "}"
        )
        self.lb_tempoAtendimento.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.lb_tempoAtendimento)

        self.lb_tempoSolucao = QLabel(self.item_chamado)
        self.lb_tempoSolucao.setObjectName("lb_tempoSolucao")
        self.lb_tempoSolucao.setMinimumSize(QSize(120, 0))
        self.lb_tempoSolucao.setMaximumSize(QSize(120, 16777215))
        self.lb_tempoSolucao.setFont(font)
        self.lb_tempoSolucao.setStyleSheet(
            "QLabel{\n" "	color: black;\n" "	border: none\n" "}"
        )
        self.lb_tempoSolucao.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.lb_tempoSolucao)

        self.lb_categoria = QLabel(self.item_chamado)
        self.lb_categoria.setObjectName("lb_categoria")
        self.lb_categoria.setMinimumSize(QSize(120, 0))
        self.lb_categoria.setMaximumSize(QSize(120, 16777215))
        self.lb_categoria.setFont(font)
        self.lb_categoria.setStyleSheet(
            "QLabel{\n" "	color: black;\n" "	border: none\n" "}"
        )
        self.lb_categoria.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.lb_categoria)

        self.lb_data_criacao = QLabel(self.item_chamado)
        self.lb_data_criacao.setObjectName("lb_data_criacao")
        self.lb_data_criacao.setMinimumSize(QSize(120, 0))
        self.lb_data_criacao.setMaximumSize(QSize(120, 16777215))
        self.lb_data_criacao.setFont(font)
        self.lb_data_criacao.setStyleSheet(
            "QLabel{\n" "	color: black;\n" "	border: none\n" "}"
        )
        self.lb_data_criacao.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.lb_data_criacao)

        self.lb_ultima_atualizacao = QLabel(self.item_chamado)
        self.lb_ultima_atualizacao.setObjectName("lb_ultima_atualizacao")
        self.lb_ultima_atualizacao.setMinimumSize(QSize(120, 0))
        self.lb_ultima_atualizacao.setMaximumSize(QSize(120, 16777215))
        self.lb_ultima_atualizacao.setFont(font)
        self.lb_ultima_atualizacao.setStyleSheet(
            "QLabel{\n" "	color: black;\n" "	border: none\n" "}"
        )
        self.lb_ultima_atualizacao.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.lb_ultima_atualizacao)

        self.horizontalLayout.addWidget(self.item_chamado)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.lb_id.setText(QCoreApplication.translate("Form", "12345", None))
        self.lb_titulo.setText(
            QCoreApplication.translate(
                "Form",
                "Chamado Teste do ChamadoChamado Teste do ChamadoChamado Teste do ChamadoChamado Teste do Chamado",
                None,
            )
        )
        self.lb_status.setText(
            QCoreApplication.translate("Form", "Ativo", None)
        )
        self.lb_tempoAtendimento.setText(
            QCoreApplication.translate("Form", "15/12/1999", None)
        )
        self.lb_tempoSolucao.setText(
            QCoreApplication.translate("Form", "15/12/1999", None)
        )
        self.lb_categoria.setText(
            QCoreApplication.translate("Form", "Impressora", None)
        )
        self.lb_data_criacao.setText(
            QCoreApplication.translate("Form", "15/12/1999", None)
        )
        self.lb_ultima_atualizacao.setText(
            QCoreApplication.translate("Form", "15/12/1999", None)
        )

    # retranslateUi
