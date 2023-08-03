import sys
import subprocess
import os
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSystemTrayIcon
from models.HomeModel import HomeModel
from views.HomeView import HomeView
from controllers.HomeController import HomeController

def executar_arquivo_exe():
    caminho_do_exe = 'update.exe'
    try:
        subprocess.Popen(caminho_do_exe)
    except FileNotFoundError:
        print("Arquivo .exe não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao executar o arquivo .exe: {e}")

def parse_args():
    return '-updated' in sys.argv

if __name__ == "__main__":
    if not parse_args():
        executar_arquivo_exe()
        sys.exit(0)

    root = QApplication(sys.argv)
    app = HomeView()
    app.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowTitleHint | Qt.CustomizeWindowHint)

    # Instanciar o controlador (HomeController) e o modelo (HomeModel)
    app = HomeController(app, HomeModel())
    root.setQuitOnLastWindowClosed(False)
    icon = QIcon("interface/images/icon.ico")
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)
    tray.activated.connect(app.show)

    root.exec_()
