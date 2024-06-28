from PySide6.QtWidgets import QDialog

from ui.login_ui import Ui_LoginPage
from windows.client import Client


class LoginChat(QDialog, Ui_LoginPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_btn.clicked.connect(self.open_chat)

    def open_chat(self):
        self.name = self.name_lineEdit.text()
        if self.name:
            self.accept()

