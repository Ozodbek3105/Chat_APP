import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel

class PopupDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pop-up Window")
        self.setGeometry(100, 100, 200, 100)
        layout = QVBoxLayout()

        message_label = QLabel("This is a pop-up window!")
        layout.addWidget(message_label)

        self.setLayout(layout)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            # Check if the mouse click is outside the dialog
            if not self.rect().contains(event.pos()):
                self.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 400, 300)

        self.button = QPushButton("Open Pop-up", self)
        self.button.setGeometry(150, 130, 100, 30)
        self.button.clicked.connect(self.show_popup)

    def show_popup(self):
        self.dialog = PopupDialog()
        self.dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
