# PyQt5 Buttons

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.button = QPushButton("Click here", self)
        self.label = QLabel("Hello", self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(100, 100, 200, 200)
        self.button.setStyleSheet("font-size : 30px;")
        self.button.clicked.connect(self.button_clicked)

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size : 30px;")


    def button_clicked(self):
        # print("Button clicked")
        # self.button.setText("Clicked")
        # self.button.setDisabled(True)
        self.label.setText("Good bye")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
