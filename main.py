from PySide6.QtWidgets import QApplication

from login_page import LoginChat
# from client.windows.client import Client

from windows.client import Client

app = QApplication()

window = LoginChat()
res = window.exec()

if res == LoginChat.Accepted:
    # print(window.name)
    chat = Client(window.name)
    chat.show()

app.exec()
