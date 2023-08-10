from base_class import Model, View


class Controller:
    def __init__(self, view, model, msg) -> None:
        self._view = view
        self._model = model
        self._msg = msg

    def show(self):
        self._view.show()

    def showMaximized(self):
        self._view.showMaximized()

    def close(self):
        self._view.close()
