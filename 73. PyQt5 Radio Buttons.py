# PyQt5 Radio Buttons

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("Gift Card", self)
        self.radio4 = QRadioButton("Off-line", self)
        self.radio5 = QRadioButton("Online", self)
        self.b_g1 = QButtonGroup(self)
        self.b_g2 = QButtonGroup(self)
        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(20, 0, 500, 100)
        self.radio2.setGeometry(20, 50, 500, 100)
        self.radio3.setGeometry(20, 100, 500, 100)
        self.radio4.setGeometry(20, 150, 500, 100)
        self.radio5.setGeometry(20, 200, 500, 100)

        self.setStyleSheet("QRadioButton{"
                           "font-size:30px;"
                           "font-family:Verdana;"
                           "padding:10px;"
                           "}")

        self.b_g1.addButton(self.radio1)
        self.b_g1.addButton(self.radio2)
        self.b_g1.addButton(self.radio3)
        self.b_g2.addButton(self.radio4)
        self.b_g2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())