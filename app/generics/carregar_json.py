import json


def read_json(file: str = "tokens.json") -> dict:
    with open(file) as file:
        tokens = json.load(file)
        return tokens


def salvar_json(
    dados: dict = {
        "user_Token": "",
        "app_Token": "",
        "url": "https://suporte.techsize.com.br/apirest.php/",
    },
    file: str = "tokens.json",
) -> None:
    with open(file, "w") as f:
        json.dump(dados, f)
