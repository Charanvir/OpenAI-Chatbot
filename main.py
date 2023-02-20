import sys

from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)

        # will not be using a central widget, but can specify self as an argument
        # This will add each of the widgets to self (the main window)

        # Add chat area widget
        # Used for bigger text
        self.chatArea = QTextEdit(self)
        # 10 pixels from left border of main window
        # 10 pixels from upper border of main window
        # 480 width of the widget
        # 320 is height of the widget
        self.chatArea.setGeometry(10, 10, 480, 320)
        self.chatArea.setReadOnly(True)

        # Add the input field
        # Used for smaller text
        self.inputField = QLineEdit(self)
        self.inputField.setGeometry(10, 340, 480, 40)

        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)

        self.show()


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
