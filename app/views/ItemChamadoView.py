import socket
from datetime import datetime

from base_class.View import View
from interface.item_chamado import Ui_Form


class ItemChamadoView(View, Ui_Form):
    def __init__(self, dados, info, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self._dados = dados
        self._info = info
        self._status = info["model"].all_status
        self._view = info["view"]
        self._model = info["model"]
        self._detalhes = info["detalhes"]

        self.definir()
        self._id = self._dados["2"]

        self.mouseDoubleClickEvent = lambda x: self.detalhes(self.id)

    def detalhes(self, id) -> None:
        self._view.stackedWidget.setCurrentIndex(1)
        self._detalhes.definir_dados(self._model.get_chamado(id))

    @property
    def dados(self):
        return self._dados

    def definir_borda(self) -> None:
        color = "blue"
        color = {
            1: "#00E300",
            2: "#ffcb7d",
            3: "#666032",
            4: "#0063E6",
            5: "#4C01E6",
            6: "#E6000E",
        }

        style = f"border-left: 5px solid {color[self._dados['12']]};"

        self.item_chamado.setStyleSheet(
            "QFrame{border-radius: 0;border: none;"
            + style
            + "border-bottom: 1px solid rgb(222, 221, 218);"
            "background-color: none; color: white;}"
            "QFrame{background-color: rgb(195, 215, 239);}"
        )

    @property
    def id(self):
        return self._id

    def definir(self) -> None:
        self.definir_borda()
        self.lb_id.setText(f"#{self._dados.get('2')}")
        try:
            self.lb_titulo.setText(
                str(self._dados.get("1")).replace(
                    f"/{socket.gethostname()}", ""
                )
            )
        except:
            self.lb_titulo.setText(str(self._dados.get("1")))
        self.lb_status.setText(self._status[self._dados.get("12")])
        self.lb_categoria.setText(str(self._dados.get("7")))
        self.lb_data_criacao.setText(
            str(
                datetime.strptime(
                    self._dados.get("15"), "%Y-%m-%d %H:%M:%S"
                ).strftime("%d/%m/%Y %H:%M")
            )
        )
        self.lb_ultima_atualizacao.setText(
            str(
                datetime.strptime(
                    self._dados.get("19"), "%Y-%m-%d %H:%M:%S"
                ).strftime("%d/%m/%Y %H:%M")
            )
        )
        self.lb_tempoSolucao.setText(
            str(
                datetime.strptime(
                    self._dados.get("18"), "%Y-%m-%d %H:%M:%S"
                ).strftime("%d/%m/%Y %H:%M")
            )
            if self._dados.get("18") != None
            else ""
        )
        self.lb_tempoAtendimento.setText(
            str(
                datetime.strptime(
                    self._dados.get("155"), "%Y-%m-%d %H:%M:%S"
                ).strftime("%d/%m/%Y %H:%M")
            )
            if self._dados.get("155") != None
            else ""
        )
