from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon

from base_class.View import View
from interface.main import Ui_Main


class HomeView(View, Ui_Main):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowTitle("Client Help Desk")
        self.setWindowIcon(QIcon(".//interface/images/icone_sistema.png"))
        self.toggle.setIcon(QIcon(".//interface/images/Logo_Techsize.png"))
        self.toggle.setIconSize(QSize(130, 130))
        self._buttons = {1: self.btn_chamados, 2: self.btn_abrirChamado}


    def definir_user(self, userName, fullName, tipo2):
        self.btn_user.setText(userName)
        self.lb_tipo1.setText(fullName)
        self.lb_tipo2.setText(tipo2)

    def nome_maquina(self, dados):
        self.lb_titulo_2.setText(dados)

    def definir_titulo(self, titulo: str = ""):
        self.lb_titulo.setText(titulo)

    def navegar(self, index: int, titulo: str) -> None:
            

        self.definir_titulo(titulo)
        button = self._buttons[index]

        self.stackedWidget.setCurrentIndex(index)
        self.lb_msg.setMaximumHeight(0)
