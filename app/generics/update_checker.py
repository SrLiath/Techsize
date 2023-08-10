import requests
import json
import subprocess
import os
from typing import Dict, Any

MANIFEST_URL = "https://raw.githubusercontent.com/pederneiranderson/ClientDesktopGLPI-updates-repository/main/versions.json"  # noqa
UPDATE_REPOSITORY_URL = (
    "https://github.com/pederneiranderson/ClientDesktopGLPI-updates-repository"
)
FILE_NAME = "Client Help Desk-{version}-win64.msi"


def check_for_update() -> Dict[str, Any]:
    message = "Falha na verificação de atualização."
    update_available = False
    latest_version = ""

    response = requests.get(MANIFEST_URL)
    if response.status_code == 200:
        manifest = json.loads(response.content)

        current_version = json.loads(open("version.json").read())["version"]
        latest_version = manifest.get("version", current_version)

        if current_version != latest_version:
            current_version_size = int(current_version.replace(".", ""))
            latest_version_size = int(latest_version.replace(".", ""))

            if current_version_size < latest_version_size:
                message = f"Versão {latest_version} disponível para download."
                update_available = True

            elif current_version_size > latest_version_size:
                message = "Você está usando uma versão mais recente que a disponível no repositório."

        else:
            message = "O sistema já está atualizado."

    return {
        "update_available": update_available,
        "message": message,
        "latest_version": latest_version,
    }


def download_update() -> None:
    update_data = check_for_update()
    if update_data["update_available"]:
        subprocess.run(["git", "clone", "-b", update_data["latest_version"], UPDATE_REPOSITORY_URL])


def install_update() -> None:
    update_data = check_for_update()
    if update_data["update_available"]:
        if os.path.exists(FILE_NAME.format(version=update_data["latest_version"])):
            subprocess.run(["msiexec", "/i", FILE_NAME, "/quiet"])
        else:
            print("Arquivo de atualização não encontrado.")


if __name__ == "__main__":
    print(check_for_update())
    download_update()
    install_update()
