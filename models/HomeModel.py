import socket

from base_class.Model import Model
from models.ApiModel import Api


class HomeModel(Model):
    def __init__(self):
        super().__init__()

        self._api = None
        self._maquina = socket.gethostname()

    @property
    def get_maquina(self):
        return self._maquina

    def iniciar_sessao(self, token_API, token_USER, url):
        self._api = Api(url, token_USER, token_API)
        self._api.iniciar_sessao()

    @property
    def get_user(self):
        return self._api.user

    @property
    def api(self):
        return self._api
