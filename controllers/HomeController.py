from base_class.Controller import Controller
from controllers.AbrirChamadoController import AbrirChamadoController
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize


# Controllers
from controllers.ChamadosController import ChamadosController
from controllers.DownloadsController import DownloadsController
from controllers.TokensController import TokensController
from generics import carregar_json

# Models
from models.AbrirChamadoModel import AbrirChamadoModel
from models.ChamadoModel import ChamadoModel
from models.DownloadsModel import DownloadsModel
from models.TokensModel import TokensModel
from views.AbrirChamadoView import AbrirChamadoView

# Views
from views.ChamadoView import ChamadosView
from views.DownloadsView import DownloadsView
from views.TokensView import TokensView


class HomeController(Controller):
    def __init__(self, view, model, msg=None) -> None:
        super().__init__(view, model, msg=None)
        self.chamados_controller = None
        self.abrir_chamado_controller = None

        if not self.verificar_tokens():
            self._controllerToken.show()
        else:
            self.start()

    def start(self):
        self.showMaximized()
        self.iniciar_sessao()
        self.definir_user()
        self.definir_maquina()

        self.chamados_controller = ChamadosController(
            ChamadosView(),
            ChamadoModel(self._model.api),
            self._view.lb_msg,
        )

        self.abrir_chamado_controller = AbrirChamadoController(
            AbrirChamadoView(),
            AbrirChamadoModel(self._model.api),
            self._view.lb_msg,
            self,
        )

        self._telas = {
            1: self.chamados_controller,
            2: self.abrir_chamado_controller,
        }

        self.definir_telas()

        self._view.btn_chamados.clicked.connect(
            lambda: self.navegar(1, "Chamados")
        )
        self._view.btn_abrirChamado.clicked.connect(
            lambda: self.navegar(2, "Abrir Chamado")
        )
        
        self.go_to_default_screen()
         # Conectando os sinais dos botões às funções correspondentes
        self._view.btn_minimize.clicked.connect(self.minimize_window)
        self._view.btn_close.clicked.connect(self.close_window)
        self._view.exit.clicked.connect(self.close_window)
        self._view.btn_maximize_restore.clicked.connect(self.maximize_restore_window)
        self._view.btn_toggle_menu.clicked.connect(self.menu)

    def menu(self):
        if self._view.side_bar.width() == 60:
            self._view.side_bar.setFixedWidth(200)
            icon = QIcon()
            icon.addFile("interface/images/Logo_Techsize.png", QSize(), QIcon.Normal, QIcon.Off)
            self._view.btn_toggle_menu_2.setIcon(icon)
            self._view.btn_toggle_menu_2.setIconSize(QSize(200, 55))
        else:
            self._view.side_bar.setFixedWidth(60)
            icon = QIcon()
            icon.addFile("interface/images/icone_sistema.png", QSize(), QIcon.Normal, QIcon.Off)
            self._view.btn_toggle_menu_2.setIcon(icon)
            self._view.btn_toggle_menu_2.setIconSize(QSize(55, 55))


    def minimize_window(self):
        # Minimizar a janela
        self._view.showMinimized()

    def close_window(self):
        # Fechar a janela
        self._view.close()

    def maximize_restore_window(self):
        if self._view.isMaximized():
            # Se a janela estiver maximizada, restaurar o tamanho original
            self._view.showNormal()

        else:
            # Se a janela não estiver maximizada, maximizar
            self._view.showMaximized()



    def go_to_default_screen(self):
        self.chamados_controller.chamados()
        self._view.btn_chamados.click()

    def navegar(self, index, msg):
        self._telas[2].limpar()
        self._telas[1].home()
        self._view.navegar(index, msg)

    def verificar_tokens(self) -> bool:
        tokens = carregar_json.read_json()
        self._controllerToken = TokensController(
            TokensView(tokens), TokensModel(tokens["url"], tokens), self
        )
        if tokens["user_Token"] == "" or tokens["app_Token"] == "":
            return False
        else:
            if self._controllerToken.testar_tokens(tokens) is True:
                self._tokenAPI = tokens["app_Token"]
                self._tokenUSER = tokens["user_Token"]
                self._url = tokens["url"]
                return True
            else:
                return False

    def iniciar_sessao(self):
        self._model.iniciar_sessao(self._tokenAPI, self._tokenUSER, self._url)

    def definir_telas(self):
        window = self._view.stackedWidget

        for index, tela in self._telas.items():
            window.insertWidget(index, tela._view)
        window.setCurrentIndex(0)

    def definir_maquina(self):
        self._view.nome_maquina(self._model.get_maquina)

    def definir_user(self):
        profiles = self._model.api.get_profiles()
        for i in profiles.keys():
            profile = profiles[i]
            break
        try:
            for i in profile["entities"].values():
                entidade = i
        except:
            for i in profile["entities"]:
                entidade = i
        self._view.definir_user(
            self._model.api.user(),
            self._model.api.full_name(),
            entidade["name"],
        )
