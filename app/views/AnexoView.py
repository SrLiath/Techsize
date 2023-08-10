from base_class.View import View
from interface.anexo import Ui_Form


class AnexoView(View, Ui_Form):
    def __init__(self, anexo: str, anexos: [str], parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self._anexos = anexos
        self._anexo = anexo
        self.anexo()

        self.pushButton.clicked.connect(lambda: self.remover())

    def remover(self):
        self._anexos.pop(self._anexos.index(self._anexo))
        self.close()

    def anexo(self):
        anexo = self._anexo.split("/")
        self.label_7.setText(anexo[-1])

    @property
    def get_anexo(self):
        return self._anexo
