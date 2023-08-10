from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QFileDialog

from base_class.Controller import Controller


class AbrirChamadoController(Controller):
    def __init__(self, view, model, msg, home) -> None:
        super().__init__(view, model, msg)

        self._view.btn_adicionar.clicked.connect(lambda: self.criar_ticket())
        self._view.btn_anexo.clicked.connect(lambda: self.adicionar_anexo())
        self.__home = home

    def limpar(self):
        self._view.limpar(
            self._msg, self._model.all_urgencia, self._model.all_categoria()
        )
        self._model.limpar_anexos()

    def adicionar_anexo(self):
        file = QFileDialog.getOpenFileName()[0]
        if file in self._model.get_anexos:
            self._view.mensagem(
                self._msg, "Anexo já adicionado.", True, "error"
            )
        elif file != "":
            self._view.mensagem(self._msg, "", False, "error")
            self._anexos = self._view.preencher_anexos(
                self._model.adicionar_anexo(file)
            )

    def preencher_campos(self):
        self._view.preencher_cb(
            self._view.cb_urgencia, self._model.all_urgencia
        )

    def criar_ticket(self):
        if self._view.status is False:
            self._view.mensagem(
                self._msg, "Preencha os campos corretamente!", True, "error"
            )
            return

        dados = self._view.get_dados

        for j, i in self._model.all_urgencia.items():
            if i == dados["urgency"]:
                dados["urgency"] = j

        categories = self._model.all_categoria()

        category_id = categories.get(dados["category"], {})

        if dados["subcategory"] != "":
            category_id = category_id.get("childs", {}).get(
                dados["subcategory"], {}
            )

            if dados["action_subcategory"] != "":
                category_id = category_id.get("childs", {}).get(
                    dados["action_subcategory"], {}
                )

        ticket = {
            "requester_full_name": dados["requester_full_name"],
            "name": dados["name"],
            "content": dados["content"],
            "priority": "3",
            "itilcategories_id": str(category_id.get("id", "")),
            "urgency": str(dados["urgency"]),
            "impact": "3",
            "type": "2",
            "status": "1",
        }

        ticket = self._model.abrir_chamado(ticket)

        try:
            self._model.adicionar_item(ticket["id"])
        except:
            pass

        if len(self._model.get_anexos) != 0:
            self._model.adicionar_anexos(ticket["id"])

        self._view.limpar(
            self._msg, self._model.all_urgencia, self._model.all_categoria()
        )
        self._model.limpar_anexos()
        self._view.mensagem(
            self._msg,
            "Chamado Aberto com Sucesso! Redirecionando...",
            True,
            "success",
            3,
        )
        QTimer.singleShot(3000, self.__home.go_to_default_screen)
