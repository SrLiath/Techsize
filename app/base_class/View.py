from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget


SECONDS_TO_MILISECONDS = 1000


class View(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def mensagem(
        self, lb, texto: str, status: bool, tipo: str, time_in_display: int = 5
    ) -> None:
        """tipo = [error, success]"""
        time_in_display = time_in_display * SECONDS_TO_MILISECONDS
        lb.setText(texto)
        tipos = {
            "success": "QLabel{color:white;background-color:rgb(87, 227, 137);border-radius: 5px;margin: 0px 40px;padding: 10px;}",
            "error": "QLabel{color:white;background-color:rgb(237, 51, 59);border-radius: 5px;margin: 0px 40px;padding: 10px;}",
        }
        lb.setStyleSheet(tipos[tipo])

        if status:
            lb.setMaximumHeight(50)
            lb.setVisible(True)
            QTimer.singleShot(
                time_in_display, lambda: lb.setVisible(False)
            )  # Dessa forma a mensagem some depois do tempo definido
        else:
            lb.setMaximumHeight(0)
