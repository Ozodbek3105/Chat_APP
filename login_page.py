from PySide6.QtWidgets import QWidget

from ui.login_ui import Ui_LoginPage
from windows.client import Client


class LoginChat(QWidget, Ui_LoginPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_btn.clicked.connect(self.open_chat)

    def open_chat(self):
        if self.name_lineEdit.text():
            self.chat = Client(self.name_lineEdit.text())
            self.chat.show()

