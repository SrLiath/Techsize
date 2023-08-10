import sys
import subprocess
import psutil
import os
import socket
import requests
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSystemTrayIcon
from models.HomeModel import HomeModel
from views.HomeView import HomeView
from controllers.HomeController import HomeController

def executar_arquivo_exe():
    caminho_do_exe = 'py\pythonw.exe Atualizacao.pyw'
    try:
        subprocess.Popen(caminho_do_exe)
    except FileNotFoundError:
        print("Arquivo .exe não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao executar o arquivo .exe: {e}")

def parse_args():
    return '-updated' in sys.argv

def check():
    server_address = ('localhost', 37548)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect(server_address)
            message = "open"
            client_socket.send(message.encode('utf-8'))
            data = client_socket.recv(1024)
            answer = data.decode('utf-8')
            if answer == "conectado":
                return True
            else:
                return False
        except:
            return False


if __name__ == "__main__":
    if check():
        sys.exit(0)
    if not parse_args():
        executar_arquivo_exe()
        sys.exit(0)
    root = QApplication(sys.argv)
    app = HomeView()
    app.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowTitleHint | Qt.CustomizeWindowHint)

    app = HomeController(app, HomeModel())
    root.setQuitOnLastWindowClosed(False)
    icon = QIcon("interface/images/icon.ico")
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)
    tray.activated.connect(app.show)
    root.exec_()
    