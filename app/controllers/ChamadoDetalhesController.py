from datetime import datetime

from base_class.Controller import Controller


class ChamadoDetalhesController(Controller):
    def __init__(self, view, model, msg) -> None:
        super().__init__(view, model, msg)

        self._dados = None

    def definir_dados(self, dados):
        self._dados = dados
        inputs = self.get_inputs(dados)
        chat = self._model.get_respostas(str(dados["id"]))
        self._view.preencher_dados(
            self._dados, self._model.get_user, inputs, chat
        )

    def get_inputs(self, dados):
        tech = self._model.get_tecnico(dados["id"])
        try:
            atendimento = datetime.strptime(
                dados["time_to_own"], "%Y-%m-%d %H:%M:%S"
            ).strftime("%d/%m/%Y %H:%M")
            solucao = datetime.strptime(
                dados["time_to_resolve"], "%Y-%m-%d %H:%M:%S"
            ).strftime("%d/%m/%Y %H:%M")
        except:
            atendimento = ""
            solucao = ""
        return {
            "abrtura": datetime.strptime(
                dados["date"], "%Y-%m-%d %H:%M:%S"
            ).strftime("%d/%m/%Y %H:%M"),
            "atualizacao": datetime.strptime(
                dados["date_mod"], "%Y-%m-%d %H:%M:%S"
            ).strftime("%d/%m/%Y %H:%M"),
            "categoria": self._model.get_categoria(dados["itilcategories_id"]),
            "status": self._model.get_status()[dados["status"]],
            "tecnico": tech["fullName"],
            "atendimento": atendimento,
            "solucao": solucao,
            "sigla": tech["sigla"],
            "urgencia": self._model.get_urgencia()[dados["urgency"]],
        }

    def definir_chat(self):
        dados = self._model.get_chat(self._dados["id"])
