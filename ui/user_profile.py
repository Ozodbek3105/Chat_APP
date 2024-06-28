from PySide6.QtWidgets import QWidget

from ui.user_profile_ui import Ui_User


class User(QWidget, Ui_User):
    def __init__(self,name,picture=None):
        super().__init__()
        self.setupUi(self)
        self.name_lbl.setText(name)
