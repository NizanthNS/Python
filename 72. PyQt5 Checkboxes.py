# PyQt5 Checkboxes

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt, QRect


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.checkBox = QCheckBox("Do you have a good time?", self)
        self.initUI()


    def initUI(self):
        self.checkBox.setGeometry(QRect(10, 0, 500, 200))
        self.checkBox.setStyleSheet("font-size: 30px;"
                                    "font-family: Verdana;")
        self.checkBox.setChecked(False)
        self.checkBox.stateChanged.connect(self.checkbox_ticked)

    def checkbox_ticked(self, state):
        if state == Qt.Checked:
            print("Not a Good Time")
        else:
            print("A worst Time")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())