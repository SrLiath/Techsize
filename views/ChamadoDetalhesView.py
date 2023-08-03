from base_class.View import View
from interface.chamado_detalhes import Ui_Form


class ChamadoDetalhesView(View, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
