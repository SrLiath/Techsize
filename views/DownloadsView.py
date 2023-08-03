from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon

from base_class.View import View
from interface.downloads import Ui_Form


class DownloadsView(View, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.link_1.setOpenExternalLinks(True)
        self.link_1.setText(
            "<a href='https://techsize.com.br/downloads/'>Baixar</a>"
        )
        self.img_1.setIcon(QIcon(".//interface/images/icone_sistema.png"))
        self.img_1.setIconSize(QSize(100, 100))
