from base_class.Model import Model


class ChamadoDetalhesModel(Model):
    def __init__(self, api):
        super().__init__()

        self._api = api

    @property
    def get_user(self):
        return self._api.user()

    def get_categoria(self, id: int) -> dict:
        return self._api.get_categoria(id)["completename"]

    def get_urgencia(self) -> str:
        return self._api.all_urgencia

    def get_status(self) -> str:
        return self._api.all_status

    def get_respostas(self, id) -> str:
        return self._api.get_respostas(id)

    def get_tecnico(self, id):
        url = f"Ticket/{id}/Ticket_User/"
        return self._api.get_ticket_users(url)
