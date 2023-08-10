# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'xdp-main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import files_rc

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(1104, 487)
        Main.setStyleSheet(u"background-color: rgb(234, 237, 241);\n"
"font-family: \"Segoe UI\";")
        self.verticalLayout_2 = QVBoxLayout(Main)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.content = QWidget(Main)
        self.content.setObjectName(u"content")
        self.horizontalLayout = QHBoxLayout(self.content)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_bar = QFrame(self.content)
        self.side_bar.setObjectName(u"side_bar")
        self.side_bar.setMaximumSize(QSize(60, 16777215))
        self.side_bar.setStyleSheet(u"	background-color: rgb(27, 29, 35);")
        self.side_bar.setFrameShape(QFrame.NoFrame)
        self.side_bar.setFrameShadow(QFrame.Raised)
        self.layout_menus_3 = QVBoxLayout(self.side_bar)
        self.layout_menus_3.setSpacing(0)
        self.layout_menus_3.setObjectName(u"layout_menus_3")
        self.layout_menus_3.setContentsMargins(0, 0, 0, 0)
        self.toggle = QPushButton(self.side_bar)
        self.toggle.setObjectName(u"toggle")
        self.toggle.setMinimumSize(QSize(10, 0))
        self.toggle.setMaximumSize(QSize(0, 0))
        self.toggle.setStyleSheet(u"QPushButton {\n"
"	background: none;\n"
"	border: none;\n"
"\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	padding: 3px;\n"
"}")

        self.layout_menus_3.addWidget(self.toggle)

        self.burguer = QFrame(self.side_bar)
        self.burguer.setObjectName(u"burguer")
        self.burguer.setFrameShape(QFrame.StyledPanel)
        self.burguer.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.burguer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.layout_menus_3.addWidget(self.burguer)

        self.btn_toggle_menu_2 = QPushButton(self.side_bar)
        self.btn_toggle_menu_2.setObjectName(u"btn_toggle_menu_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu_2.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu_2.setSizePolicy(sizePolicy)
        self.btn_toggle_menu_2.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.btn_toggle_menu_2.setFont(font)
        self.btn_toggle_menu_2.setLayoutDirection(Qt.LeftToRight)
        self.btn_toggle_menu_2.setStyleSheet(u"QPushButton {\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile("interface/images/icone_sistema.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle_menu_2.setIcon(icon)
        self.btn_toggle_menu_2.setIconSize(QSize(55, 55))

        self.layout_menus_3.addWidget(self.btn_toggle_menu_2)

        self.btn_toggle_menu = QPushButton(self.side_bar)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setMinimumSize(QSize(0, 60))
        self.btn_toggle_menu.setFont(font)
        self.btn_toggle_menu.setLayoutDirection(Qt.LeftToRight)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"background-image: url(interface/images/icons/images/icon_menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"color:white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.layout_menus_3.addWidget(self.btn_toggle_menu)

        self.btn_chamados = QPushButton(self.side_bar)
        self.btn_chamados.setObjectName(u"btn_chamados")
        sizePolicy.setHeightForWidth(self.btn_chamados.sizePolicy().hasHeightForWidth())
        self.btn_chamados.setSizePolicy(sizePolicy)
        self.btn_chamados.setMinimumSize(QSize(0, 60))
        self.btn_chamados.setFont(font)
        self.btn_chamados.setLayoutDirection(Qt.LeftToRight)
        self.btn_chamados.setStyleSheet(u"QPushButton {	\n"
"background-image: url(interface/images/icons/images/cil-home.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 23px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 23px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 23px solid rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../.designer/images/cil-home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_chamados.setIcon(icon1)

        self.layout_menus_3.addWidget(self.btn_chamados)

        self.btn_abrirChamado = QPushButton(self.side_bar)
        self.btn_abrirChamado.setObjectName(u"btn_abrirChamado")
        sizePolicy.setHeightForWidth(self.btn_abrirChamado.sizePolicy().hasHeightForWidth())
        self.btn_abrirChamado.setSizePolicy(sizePolicy)
        self.btn_abrirChamado.setMinimumSize(QSize(0, 60))
        self.btn_abrirChamado.setFont(font)
        self.btn_abrirChamado.setLayoutDirection(Qt.LeftToRight)
        self.btn_abrirChamado.setStyleSheet(u"QPushButton {	\n"
"background-image: url(interface/images/icons/images/cil-file.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 23px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 23px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 23px solid rgb(85, 170, 255);\n"
"}")

        self.layout_menus_3.addWidget(self.btn_abrirChamado)

        self.exit = QPushButton(self.side_bar)
        self.exit.setObjectName(u"exit")
        sizePolicy.setHeightForWidth(self.exit.sizePolicy().hasHeightForWidth())
        self.exit.setSizePolicy(sizePolicy)
        self.exit.setMinimumSize(QSize(0, 60))
        self.exit.setFont(font)
        self.exit.setLayoutDirection(Qt.LeftToRight)
        self.exit.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(interface/images/icons/images/cil-x.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 23px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"color:white;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 23px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 23px solid rgb(85, 170, 255);\n"
"}\n"
"")

        self.layout_menus_3.addWidget(self.exit)

        self.verticalSpacer = QSpacerItem(30, 83, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.layout_menus_3.addItem(self.verticalSpacer)

        self.frame = QFrame(self.side_bar)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_user = QLabel(self.frame)
        self.btn_user.setObjectName(u"btn_user")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_user.sizePolicy().hasHeightForWidth())
        self.btn_user.setSizePolicy(sizePolicy1)
        self.btn_user.setMinimumSize(QSize(40, 40))
        self.btn_user.setMaximumSize(QSize(40, 40))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(5)
        font1.setKerning(True)
        self.btn_user.setFont(font1)
        self.btn_user.setStyleSheet(u"	border-radius: 25px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);")
        self.btn_user.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.btn_user)


        self.layout_menus_3.addWidget(self.frame)

        self.btn_conf = QPushButton(self.side_bar)
        self.btn_conf.setObjectName(u"btn_conf")
        sizePolicy.setHeightForWidth(self.btn_conf.sizePolicy().hasHeightForWidth())
        self.btn_conf.setSizePolicy(sizePolicy)
        self.btn_conf.setMinimumSize(QSize(0, 60))
        self.btn_conf.setFont(font)
        self.btn_conf.setLayoutDirection(Qt.LeftToRight)
        self.btn_conf.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(interface/images/icons/images/cil-settings.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 23px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"color: white;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 23px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 23px solid rgb(85, 170, 255);\n"
"}\n"
"")

        self.layout_menus_3.addWidget(self.btn_conf)


        self.horizontalLayout.addWidget(self.side_bar)

        self.frame_label_bottom = QFrame(self.content)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_label_bottom)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.frame_label_bottom)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMaximumSize(QSize(16777215, 60))
        self.top_bar.setStyleSheet(u"background-color: transparent;")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.top_bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(0, 0))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.top_bar)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 30))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(33, 37, 43, 150);")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(8, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(interface/images/icons/images/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.lb_msg = QLabel(self.frame_label_top_btns)
        self.lb_msg.setObjectName(u"lb_msg")
        self.lb_msg.setMaximumSize(QSize(0, 0))

        self.horizontalLayout_10.addWidget(self.lb_msg)

        self.lb_titulo_11 = QLabel(self.frame_label_top_btns)
        self.lb_titulo_11.setObjectName(u"lb_titulo_11")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.lb_titulo_11.setFont(font2)
        self.lb_titulo_11.setStyleSheet(u"background: transparent;\n"
"margin-left: 5px;")

        self.horizontalLayout_10.addWidget(self.lb_titulo_11)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right)


        self.verticalLayout_10.addWidget(self.frame_top_btns)

        self.top_bar_2 = QFrame(self.frame_top_right)
        self.top_bar_2.setObjectName(u"top_bar_2")
        self.top_bar_2.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.top_bar_2.setFrameShape(QFrame.NoFrame)
        self.top_bar_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.top_bar_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.widget_info_3 = QWidget(self.top_bar_2)
        self.widget_info_3.setObjectName(u"widget_info_3")
        self.widget_info_3.setMinimumSize(QSize(100, 0))
        self.widget_info_3.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_11 = QHBoxLayout(self.widget_info_3)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lb_tipo2 = QLabel(self.widget_info_3)
        self.lb_tipo2.setObjectName(u"lb_tipo2")
        self.lb_tipo2.setMaximumSize(QSize(16777215, 20))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        self.lb_tipo2.setFont(font3)
        self.lb_tipo2.setStyleSheet(u"color:white;")

        self.horizontalLayout_11.addWidget(self.lb_tipo2)

        self.frame_2 = QFrame(self.widget_info_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_2)

        self.lb_tipo1 = QLabel(self.widget_info_3)
        self.lb_tipo1.setObjectName(u"lb_tipo1")
        self.lb_tipo1.setMaximumSize(QSize(16777215, 20))
        self.lb_tipo1.setFont(font3)
        self.lb_tipo1.setStyleSheet(u"color:white;")

        self.horizontalLayout_11.addWidget(self.lb_tipo1)


        self.gridLayout.addWidget(self.widget_info_3, 0, 3, 1, 1)

        self.frame_3 = QFrame(self.top_bar_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_3, 0, 2, 1, 1)

        self.lb_titulo_3 = QLabel(self.top_bar_2)
        self.lb_titulo_3.setObjectName(u"lb_titulo_3")
        self.lb_titulo_3.setMinimumSize(QSize(75, 0))
        self.lb_titulo_3.setMaximumSize(QSize(80, 20))
        self.lb_titulo_3.setFont(font2)
        self.lb_titulo_3.setStyleSheet(u"QLabel {\n"
"	color: rgb(0, 193, 255)\n"
"}")

        self.gridLayout.addWidget(self.lb_titulo_3, 0, 0, 1, 1)

        self.lb_titulo_2 = QLabel(self.top_bar_2)
        self.lb_titulo_2.setObjectName(u"lb_titulo_2")
        self.lb_titulo_2.setFont(font)
        self.lb_titulo_2.setStyleSheet(u"color:white;")

        self.gridLayout.addWidget(self.lb_titulo_2, 0, 1, 1, 1)


        self.verticalLayout_10.addWidget(self.top_bar_2)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout_3.addWidget(self.top_bar)

        self.stackedWidget = QStackedWidget(self.frame_label_bottom)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.frame_grip = QFrame(self.frame_label_bottom)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.lb_titulo = QLabel(self.frame_grip)
        self.lb_titulo.setObjectName(u"lb_titulo")
        self.lb_titulo.setMaximumSize(QSize(16777215, 20))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(8)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        font4.setKerning(True)
        self.lb_titulo.setFont(font4)
        self.lb_titulo.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_6.addWidget(self.lb_titulo)

        self.lb_titulo_6 = QLabel(self.frame_grip)
        self.lb_titulo_6.setObjectName(u"lb_titulo_6")
        self.lb_titulo_6.setMinimumSize(QSize(50, 0))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(25)
        font5.setBold(False)
        self.lb_titulo_6.setFont(font5)
        self.lb_titulo_6.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(interface/images/icons/images/cil-settings.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 23px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 23px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 23px solid rgb(85, 170, 255);\n"
"}\n"
"\n"
"")
        self.lb_titulo_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lb_titulo_6)

        self.lb_titulo_5 = QLabel(self.frame_grip)
        self.lb_titulo_5.setObjectName(u"lb_titulo_5")

        self.horizontalLayout_6.addWidget(self.lb_titulo_5)

        self.lb_titulo_4 = QLabel(self.frame_grip)
        self.lb_titulo_4.setObjectName(u"lb_titulo_4")
        self.lb_titulo_4.setMaximumSize(QSize(100, 16777215))
        self.lb_titulo_4.setFont(font)
        self.lb_titulo_4.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.lb_titulo_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.lb_titulo_4)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_3.addWidget(self.frame_grip)


        self.horizontalLayout.addWidget(self.frame_label_bottom)


        self.verticalLayout_2.addWidget(self.content)


        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Form", None))
        self.toggle.setText("")
        self.btn_toggle_menu_2.setText("")
        self.btn_toggle_menu.setText("")
        self.btn_chamados.setText(QCoreApplication.translate("Main", u"Chamados", None))
        self.btn_abrirChamado.setText(QCoreApplication.translate("Main", u"Cadastrar chamados", None))
        self.exit.setText(QCoreApplication.translate("Main", u"Sair", None))
        self.btn_user.setText(QCoreApplication.translate("Main", u"WM", None))
        self.btn_conf.setText(QCoreApplication.translate("Main", u"Configura\u00e7\u00e3o", None))
        self.lb_msg.setText("")
        self.lb_titulo_11.setText(QCoreApplication.translate("Main", u"Client Help Desk", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("Main", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("Main", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("Main", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.lb_tipo2.setText(QCoreApplication.translate("Main", u"Entidade Raiz", None))
        self.lb_tipo1.setText(QCoreApplication.translate("Main", u"Admin", None))
        self.lb_titulo_3.setText(QCoreApplication.translate("Main", u"Hostname:", None))
        self.lb_titulo_2.setText(QCoreApplication.translate("Main", u"GLPI", None))
        self.lb_titulo.setText("")
        self.lb_titulo_6.setText("")
        self.lb_titulo_5.setText("")
        self.lb_titulo_4.setText(QCoreApplication.translate("Main", u"v1.0.0", None))
    # retranslateUi

