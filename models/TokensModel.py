from base_class.Model import Model
from Ticket import Ticket


class TokensModel(Model):
    def __init__(self, url, tokens):
        super().__init__()

        self._url = url
        self._userToken = ""
        self._appToken = ""
        self._tokens = tokens

    def set_tokens(self, tokens) -> bool:
        if not tokens["user_Token"] or not tokens["app_Token"]:
            return False

        self._userToken = tokens["user_Token"]
        self._appToken = tokens["app_Token"]

        return True

    def validar_tokens(self):
        return Ticket(
            self._url, self._userToken, self._appToken
        ).iniciar_sessao()

    @property
    def tokens(self) -> dict:
        self._tokens["user_Token"] = f"{self._userToken}"
        self._tokens["app_Token"] = f"{self._appToken}"
        return self._tokens
