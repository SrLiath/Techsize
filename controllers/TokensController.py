from base_class.Controller import Controller
from generics import carregar_json
from generics.carregar_json import salvar_json
from models.TokensModel import TokensModel
from views.TokensView import TokensView


class TokensController(Controller):
    def __init__(
        self, view: TokensView, model: TokensModel, home, msg=None
    ) -> None:
        super().__init__(view, model, msg=None)
        self._home = home
        self._view.btn_cadastrar.clicked.connect(self.validar_tokens)

    def validar_tokens(self):
        token_setted = self._model.set_tokens(self._view.salvar())

        if not token_setted:
            return

        if self._model.validar_tokens().status_code != 200:
            self._view.msg_error("Erro ao validar Tokens", True)
        else:
            salvar_json(dados=self._model.tokens)
            self._view.close()
            self._home.verificar_tokens()
            self._home.start()

    def testar_tokens(self, tokens: dict):
        self._model.set_tokens(tokens)
        status = self._model.validar_tokens()
        if status.status_code != 200:
            return False
        else:
            return True
