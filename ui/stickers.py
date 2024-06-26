from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QToolButton

from ui.sticker_ui import Ui_Dialog


class Emoji(QDialog, Ui_Dialog):
    emoji = Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        for button in  [child for child in self.children() if isinstance(child, QToolButton)]:
            button.clicked.connect(self.button_clicked)

        # font = QFont("../images/NotoColorEmoji-Regular.ttf", 14)
        # self.setFont(font)


        # self.button_clicked()

    def button_clicked(self):
        button: QToolButton = self.sender()
        # print("button.text()", button.text())
        self.emoji.emit(button.text())

