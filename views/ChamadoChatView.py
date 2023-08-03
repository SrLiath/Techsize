from datetime import datetime

from bs4 import BeautifulSoup as bs

from base_class.View import View
from interface.chamado_chat import Ui_Form


class ChamadoChatView(View, Ui_Form):
    def __init__(self, dados, user, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self._dados = dados
        self._user = user

    def preencher_inicio(self):
        self.lb_descricao.setText(self._dados["content"])
        self.lb_user.setText(self._user)
        self.lb_criado.setText(
            f"Criado em: {datetime.strptime(self._dados['date_creation'], '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M')}"
        )

    def user(self):
        pass

    def preencher_resposta(self):
        self.plainTextEdit.appendHtml(bs(self._dados["content"]).text)
        self.lb_user.setText(self._user)
        self.lb_criado.setText(
            f"Criado em: {datetime.strptime(self._dados['date_creation'], '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M')}"
        )
