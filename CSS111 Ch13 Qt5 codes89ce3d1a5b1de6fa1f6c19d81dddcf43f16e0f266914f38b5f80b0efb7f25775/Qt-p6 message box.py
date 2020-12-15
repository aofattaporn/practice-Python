from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
win = QMainWindow()
win.setWindowTitle("Main Window")

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()

button = QPushButton('Click')
button.clicked.connect(on_button_clicked)
button.show()

app.exec_()