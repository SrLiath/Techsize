import json

import requests


class Ticket:
    def __init__(self, url: str, user_token: str, app_token: str):
        self._url = url
        self._user_token = user_token
        self._app_token = app_token
        self._headers = {
            "App-Token": self._app_token,
            "Content-Type": "application/json",
        }

        self._sessao = ""

    @property
    def headers(self):
        return self._headers

    def iniciar_sessao(self) -> str:
        url = self._url + "initSession/"
        headers = self.headers
        headers["Authorization"] = f"user_token {self._user_token}"
        session = requests.get(url, headers=self.headers)
        if session.status_code == 200:
            self._headers["Session-Token"] = session.json()["session_token"]
            self._sessao = session.json()["session_token"]
        return session

    def encerar_sessao(self) -> dict:
        url = self._url + "killSession/"
        return requests.get(url, headers=self.headers).json()

    def sessao(self):
        url = self._url + "getFullSession/"
        session = requests.get(url, headers=self.headers).json()
        return session["session"]

    def get_tickets(self):
        url = self._url + "Ticket/"
        return requests.get(url, headers=self.headers).json()

    def ticket(self, id: str):
        url = self._url + "Ticket/" + id + "/"
        return requests.get(url, headers=self.headers).json()

    def abrir_ticket(self, nome: str, conteudo: str):
        content = {
            "input": {
                "name": nome,
                "content": conteudo,
                "_users_id_requester": self.sessao()["glpiID"],
            }
        }
        url = self._url + "Ticket/"
        return requests.post(
            url, headers=self.headers, data=json.dumps(content)
        ).json()
