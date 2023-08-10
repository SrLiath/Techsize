from base_class.Model import Model


class ChamadoModel(Model):
    def __init__(self, api):
        super().__init__()

        self._api = api

    def get_chamados(self):
        return self._api.get_tickets()

    def get_chamados_filtro(self, filtro: int):
        return self._api.get_tickets_filtro(filtro)

    def get_id_status(self, filtro: str):
        for key, value in self.all_status.items():
            if value == filtro:
                return key

    def get_chamado(self, id):
        return self._api.ticket(str(id))

    @property
    def all_status(self) -> dict:
        return {
            1: "Novo",
            2: "Em atendimento (atribuído)",
            3: "Em atendimento (planejado)",
            4: "Pendente",
            5: "Solucionado",
            6: "Fechado",
        }

    def all_origem(self) -> [dict]:
        return self._api.get_origens()

    def get_categoria(self, id: int) -> dict:
        return self._api.get_categoria(id)["name"]

    def get_urgencia(self) -> str:
        return self._api.all_urgencia

    def get_status(self) -> str:
        return self._api.all_tipo

    def get_chat(self, id):
        return self._api.chat(id)

    def get_api(self):
        return self._api
