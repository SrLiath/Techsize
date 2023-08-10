from base_class.Controller import Controller

# Controller
from controllers.ChamadoDetalhesController import ChamadoDetalhesController

# Model
from models.ChamadoDetalhesModel import ChamadoDetalhesModel

# View
from views.ChamadoDetalhesView import ChamadoDetalhesView


class ChamadosController(Controller):
    def __init__(self, view, model, msg) -> None:
        super().__init__(view, model, msg)

        self._view.btn_atualizar.clicked.connect(lambda: self.chamados())
        self._view.cb_filtro.currentIndexChanged.connect(
            lambda: self.filtrar()
        )
        self._view.btn_voltar.clicked.connect(lambda: self.home())

        self._detalhes = ChamadoDetalhesController(
            self._view, ChamadoDetalhesModel(self._model.get_api()), self._msg
        )

        self._info = {
            "model": self._model,
            "view": self._view,
            "detalhes": self._detalhes,
        }

    def chamados(self) -> None:
        self._view.cb_filtro.setCurrentIndex(0)
        self.filtrar()

    def home(self) -> None:
        self._view.stackedWidget.setCurrentIndex(0)

    def filtrar(self) -> None:
        filtro = self._view.get_filtro
        status = self._model.get_id_status(filtro)
        if status:
            self._items = self._view.preencher_tabela(
                self._model.get_chamados_filtro(status), self._info
            )
        else:
            self._items = self._view.preencher_tabela(
                self._model.get_chamados(), self._info
            )
