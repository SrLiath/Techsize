from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon

from base_class.View import View
from interface.tokens import Ui_Form


class TokensView(View, Ui_Form):
    def __init__(self, tokens: dict, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowTitle("Client Help Desk")
        self.setWindowIcon(QIcon(".//interface/images/icone_sistema.png"))

        self.logo.setIcon(QIcon(".//interface/images/Logo_Techsize.png"))
        self.logo.setIconSize(QSize(240, 245))

        self._tokens = tokens
        self.definir_campos()

    def definir_campos(self) -> None:
        self.input_tokenUser.setText(self._tokens["user_Token"])
        self.input_tokenAPI.setText(self._tokens["app_Token"])

    def salvar(self) -> dict:
        dados = {
            "user_Token": self.input_tokenUser.text(),
            "app_Token": self.input_tokenAPI.text(),
        }

        if dados["user_Token"] == "" or dados["app_Token"] == "":
            self.msg_error("Preencha ambos os campos!", True)

        return dados

    def msg_error(self, msg: str, status: bool):
        try:
            self.error_informer_label.setText(msg)
            if status == True:
                self.error_informer_label.setMaximumHeight(30)
                self.show_error_label()
            else:
                self.error_informer_label.setMaximumHeight(0)
        except:
            pass
