from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget

from ui.message_window_ui import Ui_MessagePage


class MessagePage(QWidget, Ui_MessagePage):
    def __init__(self, me=True):
        super().__init__()
        self.setupUi(self)

        self.init_ui(me)

    def init_ui(self, me):

        if not me:
            self.setStyleSheet("background-color: white;")
            self.message_label.setAlignment(Qt.AlignLeft)
            self.name_label.setAlignment(Qt.AlignLeft)
        else:
            self.setStyleSheet("background-color: #EFFDDE;")
            self.message_label.setAlignment(Qt.AlignRight)
            self.name_label.setAlignment(Qt.AlignRight)
