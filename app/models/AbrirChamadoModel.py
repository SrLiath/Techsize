import socket

from base_class.Model import Model


class AbrirChamadoModel(Model):
    def __init__(self, api):
        super().__init__()

        self._api = api
        self._anexos: [str] = []

    def adicionar_anexo(self, anexo: str):
        self._anexos.append(anexo)
        return self._anexos

    def limpar_anexos(self):
        self._anexos: [str] = []

    @property
    def get_anexos(self) -> [str]:
        return self._anexos

    @property
    def all_tipo(self) -> dict:
        return self._api.all_tipo

    @property
    def all_urgencia(self) -> dict:
        return self._api.all_urgencia

    def all_categoria(self) -> [dict]:
        categories = self._api.get_categorias()
        return categories

    def abrir_chamado(self, ticket: dict):
        return self._api.abrir_ticket(ticket)

    def adicionar_item(self, ticket):
        return self._api.inserir_item(socket.gethostname(), ticket)

    def adicionar_anexos(self, ticket):
        for anexo in self._anexos:
            name = anexo.split("/")
            full = f"{name[-1]}"
            file = f'"{anexo}"'

            content = {
                "uploadManifest": '{"input": {"name": '
                + f'"{full}"'
                + ","
                + '"_filename":'
                + f"[{file}]"
                + "}}"
            }

            files = [
                ("filename[0]", (full, open(anexo, "rb"), "application/json"))
            ]

            doc = self._api.adicionar_documento(content, files, ticket)
