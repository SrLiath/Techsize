import socket

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSizePolicy, QSpacerItem

from base_class.View import View
from interface.chamados import Ui_Form
from views.ChamadoChatRespostaView import ChamadoChatRespostaView
from views.ChamadoChatView import ChamadoChatView
from views.ItemChamadoView import ItemChamadoView


class ChamadosView(View, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self._items = []
        self._items_chat = []
        self._space = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )
        self._space_chat = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        # self.link.setOpenExternalLinks(True)
        # self.link.setText("<a href='https://www.google.com'>LINK</a>")

    def limpar_titulo(self, titulo: str):
        try:
            return titulo.replace(f"/{socket.gethostname()}", "")
        except:
            return titulo

    @property
    def get_filtro(self):
        return self.cb_filtro.currentText()

    def adiciona_item(self, dados, info):
        item = ItemChamadoView(dados, info)
        self.verticalLayout_2.addWidget(item)
        self._items.append(item)

    def preencher_tabela(self, dados, info):
        self.limpar()
        if dados["count"] != 0:
            dados = dados["data"]
            for i in dados:
                self.adiciona_item(i, info)

            self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.scrollArea.setWidgetResizable(True)
            self.verticalLayout_2.addSpacerItem(self._space)

        return self._items

    def limpar(self):
        for i in self._items:
            i.deleteLater()
            i = None
        self._items = []
        self.verticalLayout_2.removeItem(self._space)

    # DETALHES

    def preencher_dados(self, dados, user, inputs, chat):
        self.label_4.setText(f"Chamado #{dados['id']}")
        self.inserir_ticket_inicial([dados], user)
        self.inserir_chat(chat, inputs["sigla"])
        self.preencher_inputs(inputs)
        self.verticalLayout_5.addSpacerItem(self._space)

    def preencher_inputs(self, dados):
        self.input_abertura.setText(dados["abrtura"])
        self.input_atualizacao.setText(dados["atualizacao"])
        self.input_categoria.setText(dados["categoria"])
        self.input_status.setText(dados["status"])
        self.input_tecnico.setText(dados["tecnico"])
        self.input_urgencia.setText(dados["urgencia"])
        self.input_tempoSolucao.setText(dados["solucao"])
        self.input_tempoAtendimento.setText(dados["atendimento"])

    def inserir_chat(self, dados, user):
        self.preencher_tabela_chat(dados, user, "chat")

    def inserir_ticket_inicial(self, dados, user):
        self.limpar_chat()
        self.preencher_tabela_chat(dados, user, "inicial")

    def adiciona_item_chat(self, dados, user):
        item_chat = ChamadoChatView(dados, user)
        self.verticalLayout_5.addWidget(item_chat)
        self._items_chat.append(item_chat)
        return item_chat

    def adiciona_resposta_chat(self, dados, user):
        item_chat = ChamadoChatRespostaView(dados, user)
        self.verticalLayout_5.addWidget(item_chat)
        self._items_chat.append(item_chat)
        return item_chat

    def preencher_tabela_chat(self, dados, user, tipo):
        if tipo == "inicial":
            item = self.adiciona_resposta_chat(dados[0], user)
            item.preencher_inicio()
        else:
            for i in dados:
                item = self.adiciona_item_chat(i, user)
                item.preencher_resposta()

        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        return self._items

    def limpar_chat(self):
        for i in self._items_chat:
            i.deleteLater()
            i = None
        self._items_chat = []
        self.verticalLayout_5.removeItem(self._space)
