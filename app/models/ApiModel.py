import json
import socket
from typing import List

import requests


class Api:
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

    def user(self):
        try:
            userName: str = (
                self.sessao()["glpiname"][0] + self.sessao()["glpirealname"][0]
            )
        except:
            userName = ""
        return userName.upper()

    def full_name(self):
        return self.sessao()["glpiname"]

    def iniciar_sessao(self) -> str:
        url = self._url + "initSession/"
        headers = self.headers
        ip = url.split("/")
        headers["Authorization"] = f"user_token {self._user_token}"
        session = requests.get(url, headers=self.headers)
        try:
            ip = f"{ip[0]}//{ip[2]}:62354/now"
            inventory = requests.get(ip)
        except:
            pass
        if session.status_code == 200:
            self._headers["Session-Token"] = session.json()["session_token"]
            self._sessao = session.json()["session_token"]
        return session

    def get_profiles(self):
        return self.sessao()["glpiprofiles"]

    def get_categorias(self):
        url = self._url + "ITILCategory?range=0-9000"
        categorias = requests.get(url, headers=self.headers).json()
        objetos_organizados = self.__organizar_objetos(categorias)

        return objetos_organizados

    def __organizar_objetos(self, lista_objetos):
        objetos_organizados = {}

        for obj in lista_objetos:
            nome_objeto = obj["name"]
            id_objeto = obj["id"]
            completename_objeto = obj["completename"]
            ancestors_cache = json.loads(obj["ancestors_cache"])

            if ancestors_cache:
                pais_ids = [int(key) for key in ancestors_cache]
                pais_completenames = self.__get_pais_completenames(
                    pais_ids, lista_objetos
                )
                ref = objetos_organizados

                for pai_completename in pais_completenames:
                    if pai_completename not in ref:
                        ref[pai_completename] = {
                            "id": int(pais_ids.pop(0)),
                            "completename": pai_completename,
                            "childs": {},
                        }

                    ref = ref[pai_completename]["childs"]

                ref[nome_objeto] = {
                    "id": id_objeto,
                    "completename": completename_objeto,
                    "childs": {},
                }
            else:
                objetos_organizados[nome_objeto] = {
                    "id": id_objeto,
                    "completename": completename_objeto,
                    "childs": {},
                }

        return objetos_organizados

    def __get_pais_completenames(self, pais_ids, lista_objetos) -> List[str]:
        pais_completenames = []

        for id in pais_ids:
            for obj in lista_objetos:
                if obj["id"] == id:
                    pais_completenames.append(obj["name"])

        return pais_completenames

    def get_categoria(self, id: int):
        url = self._url + f"ITILCategory/{id}"
        return requests.get(url, headers=self.headers).json()

    @property
    def all_tipo(self) -> dict:
        return {
            1: "Incidente",
            2: "Requisição",
        }

    @property
    def all_status(self) -> dict:
        return {
            1: "Novo",
            2: "Em Andamento (atribuído)",
            3: "Em Andamento (planejado)",
            4: "Pendente",
            5: "Solucionado",
            6: "Fechado",
        }

    @property
    def all_urgencia(self) -> dict:
        return {
            5: "Muito Alta",
            4: "Alta",
            3: "Média",
            2: "Baixa",
            1: "Muito Baixa",
        }

    def encerar_sessao(self) -> dict:
        url = self._url + "killSession/"
        return requests.get(url, headers=self.headers).json()

    def sessao(self):
        url = self._url + "getFullSession/"
        session = requests.get(url, headers=self.headers).json()
        return session["session"]

    def get_tickets(self):
        user_id = self.sessao()["glpiID"]
        url = self._url + f"search/Ticket"
        url += f"?criteria[1][field]=4&criteria[1][searchtype]=equals&criteria[1][value]={user_id}"
        url += f"&criteria[2][field]=1&criteria[2][searchtype]=contains&criteria[2][value]={socket.gethostname()}"
        url += f"&criteria[0][field]=155&criteria[0][searchtype]=contains&criteria[0][value]="
        url += "&order=DESC&sort=2"
        return requests.get(url, headers=self.headers).json()

    def get_tickets_filtro(self, filtro: int):
        user_id = self.sessao()["glpiID"]
        url = self._url + f"search/Ticket"
        url += f"?criteria[1][field]=4&criteria[1][searchtype]=equals&criteria[1][value]={user_id}"
        url += f"&criteria[0][field]=12&criteria[0][searchtype]=equals&criteria[0][value]={filtro}"
        url += f"&criteria[2][field]=1&criteria[2][searchtype]=contains&criteria[2][value]={socket.gethostname()}"
        url += "&order=DESC&sort=2"
        return requests.get(url, headers=self.headers).json()

    def ticket(self, id: str):
        url = self._url + "Ticket/" + id + "/"
        return requests.get(url, headers=self.headers).json()

    def abrir_ticket(self, ticket: dict):
        ticket = ticket
        ticket["_users_id_requester"] = self.sessao()["glpiID"]
        content = {"input": ticket}
        url = self._url + "Ticket/"
        return requests.post(
            url, headers=self.headers, data=json.dumps(content)
        ).json()

    def chat(self, id):
        url = self._url + "Ticket/" + id + "/"
        return requests.get(url, headers=self.headers).json()

    def adicionar_documento(self, dados, files, ticket):
        url = self._url + "Document/"
        del self._headers["Content-Type"]
        response = requests.request(
            "POST", url, headers=self._headers, data=dados, files=files
        )
        self._headers["Content-Type"] = "application/json"
        self.adicnionar_doc_ticket(response, ticket)
        return response.json()

    def adicnionar_doc_ticket(self, response, ticket):
        id = response.json()["id"]
        url = self._url + "Document/1/Document_Item/"
        payload = {
            "input": {
                "documents_id": id,
                "items_id": ticket,
                "itemtype": "Ticket",
                "users_id": "7",
            }
        }

        response = requests.request(
            "POST", url, headers=self._headers, data=json.dumps(payload)
        )

    def get_respostas(self, id):
        url = self._url + "Ticket/" + id + "/" + "ITILFollowup"
        return requests.get(url, headers=self.headers).json()

    def get_ticket_users(self, url):
        url = self._url + url
        tecnico = requests.get(url, headers=self.headers).json()
        if len(tecnico) > 1:
            try:
                tecnico = requests.get(
                    tecnico[1]["links"][1]["href"], headers=self.headers
                ).json()
                return {
                    "fullName": tecnico["firstname"]
                    + " "
                    + tecnico["realname"],
                    "sigla": tecnico["firstname"][0].upper()
                    + tecnico["realname"][0].upper(),
                }
            except:
                return {"fullName": "", "sigla": ""}
        else:
            return {"fullName": "", "sigla": ""}

    def inserir_item(self, item, ticket):
        url = (
            self._url
            + f"search/Computer?criteria[1][field]=1&criteria[1][searchtype]=contains&criteria[1][value]={item}"
        )
        url += f"&criteria[0][field]=2&criteria[0][searchtype]=contains&criteria[0][value]="
        item = (
            requests.get(url, headers=self.headers)
            .json()
            .get("data", [])[0]
            .get("2")
        )
        url = self._url + f"Item_Ticket"
        payload = {
            "input": {
                "itemtype": "Computer",
                "items_id": item,
                "tickets_id": ticket,
            }
        }
        return requests.request(
            "POST", url, headers=self._headers, data=json.dumps(payload)
        )
