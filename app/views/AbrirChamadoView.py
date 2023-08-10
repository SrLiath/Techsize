import socket

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSizePolicy, QSpacerItem

from base_class.View import View
from interface.abrir_chamado import Ui_Form
from views.AnexoView import AnexoView


class AbrirChamadoView(View, Ui_Form):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)

        self._items = []
        self._space = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

    def preencher_categoria(self, categories_data: dict) -> None:
        self.cb_categoria.clear()
        self.cb_categoria.addItem("-----")
        for category in categories_data.keys():
            self.cb_categoria.addItem(category)

        self.cb_categoria.currentIndexChanged.connect(
            lambda: self.preencher_subcategoria(categories_data)
        )

    def reset_subcategory(self) -> None:
        self.cb_subcategoria.clear()
        self.cb_subcategoria.setEnabled(False)

    def reset_action_subcategory(self) -> None:
        self.cb_action_subcategoria.clear()
        self.cb_action_subcategoria.setEnabled(False)

    def preencher_subcategoria(self, categories_data: dict) -> None:
        self.cb_subcategoria.clear()
        self.cb_subcategoria.setEnabled(True)
        self.cb_subcategoria.addItem("")
        category_selected = self.cb_categoria.currentText()
        if category_selected != "-----" and category_selected != "":
            subcategories_data = categories_data[category_selected].get(
                "childs", {}
            )
            for subcategory in subcategories_data.keys():
                self.cb_subcategoria.addItem(subcategory)

            self.cb_subcategoria.currentIndexChanged.connect(
                lambda: self.preencher_action_subcategoria(subcategories_data)
            )

    def preencher_action_subcategoria(self, subcategories_data: dict) -> None:
        self.cb_action_subcategoria.clear()
        self.cb_action_subcategoria.setEnabled(True)
        self.cb_action_subcategoria.addItem("")
        subcategory_selected = self.cb_subcategoria.currentText()
        if subcategory_selected != "":
            action_subcategories_data = subcategories_data[
                subcategory_selected
            ].get("childs", {})

            for action_subcategory in action_subcategories_data.keys():
                self.cb_action_subcategoria.addItem(action_subcategory)

    def preencher_cb(self, cb, dados: dict) -> None:
        cb.clear()
        for item in dados.values():
            cb.addItem(item)

    @property
    def nome(self) -> str:
        return self.lineEdit_nome.text()

    @property
    def titulo(self) -> str:
        return self.lb_titulo.text() + "/" + socket.gethostname()

    @property
    def descricao(self) -> str:
        return self.txt_descricao.toPlainText()

    @property
    def categoria(self) -> str:
        return self.cb_categoria.currentText()

    @property
    def urgencia(self) -> str:
        return self.cb_urgencia.currentText()

    @property
    def subcategoria(self) -> str:
        return self.cb_subcategoria.currentText()

    @property
    def action_subcategoria(self) -> str:
        return self.cb_action_subcategoria.currentText()

    def limpar(self, msg, urgencia, categoria):
        self.preencher_cb(self.cb_urgencia, urgencia)
        self.preencher_categoria(categoria)
        self.reset_subcategory()
        self.reset_action_subcategory()
        self.cb_urgencia.setCurrentIndex(2)
        self.txt_descricao.setPlainText("")
        self.lb_titulo.setText("")
        self.lineEdit_nome.setText("")
        msg.setMaximumHeight(0)
        self.limpar_anexo()

    @property
    def status(self) -> bool:
        return (
            True
            if self.nome != ""
            and self.titulo != ""
            and self.descricao != ""
            and self.categoria != "-----"
            else False
        )

    @property
    def get_dados(self):
        return {
            "requester_full_name": self.nome,
            "name": self.titulo,
            "content": self.descricao,
            "urgency": self.urgencia,
            "category": self.categoria,
            "subcategory": self.subcategoria,
            "action_subcategory": self.action_subcategoria,
        }

    def adiciona_item(self, dados, anexos):
        item = AnexoView(dados, anexos)
        self.verticalLayout_5.addWidget(item)
        self._items.append(item)

    def preencher_anexos(self, dados):
        self.limpar_anexo()
        if len(dados) != 0:
            for i in dados:
                self.adiciona_item(i, dados)

            self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.scrollArea.setWidgetResizable(True)
            self.verticalLayout_5.addSpacerItem(self._space)

        return self._items

    def limpar_anexo(self):
        for i in self._items:
            i.deleteLater()
            i = None
        self._items = []
        self.verticalLayout_5.removeItem(self._space)
