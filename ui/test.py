from PySide6.QtWidgets import QDial, QDialog

from ui.test_ui import Ui_Dialog


class Test_(QDialog, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)