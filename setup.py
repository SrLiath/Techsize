import sys
import os
from cx_Freeze import Executable, setup

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only

current_dir = os.path.dirname(sys.argv[0])

images_to_include = [
    os.path.join(current_dir, "interface/images/anydesk.png"),
    os.path.join(current_dir, "interface/images/icone_sistema.png"),
    os.path.join(current_dir, "interface/images/Logo_Techsize.png"),
    os.path.join(current_dir, "interface/resources/anydesk.png"),
    os.path.join(current_dir, "interface/resources/down-arrow.png"),
    os.path.join(current_dir, "interface/resources/images.qrc"),
]

build_exe_options = {
    "packages": ["PySide6", "requests", "bs4", "lxml"],
    "include_files": [
        "icon.ico",
        "tokens.json",
        "README.txt",
        "interface/images/",
        "interface/resources/",
        "GLPI-Agent-1.5-giteab5c585-x64.msi",
        *images_to_include,
        ],
    "include_msvcr" : True,
}

base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="Client Help Desk",
    version="1.1.1",
    fullname="Client Help Desk 1.1.1",
    description="Client Help Desk",
    options={"build_exe": build_exe_options},
    executables=[Executable(
        "main.py",
        base=base,
        target_name="Client Help Desk",
        icon="icon.ico",
        copyright="Copyright © 2022 Techsize. Todos os direitos Reservados.",
        shortcut_name="Techsize Client Help Desk",
        shortcut_dir="DesktopFolder",
    )],
)
