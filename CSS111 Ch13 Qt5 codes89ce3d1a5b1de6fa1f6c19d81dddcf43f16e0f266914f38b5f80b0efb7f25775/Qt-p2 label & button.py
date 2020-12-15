#from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
win = QMainWindow()
win.setWindowTitle("Main Window")
win.setGeometry(400, 400, 500, 300)

# a label
#
label = QLabel(win)
label.setText("My first label in my GUI program")
label.adjustSize()
label.move(100, 50)

# 1st button
#
def update():
    label.setText("Updated")

btUpdate = QPushButton(win)
btUpdate.clicked.connect(update)
btUpdate.setText("Update Button")
btUpdate.adjustSize()
btUpdate.move(100, 100)

# 2nd button
#
def display():
    print(label.text())

btDisplay = QPushButton(win)
btDisplay.clicked.connect(display)
btDisplay.setText("Display")
btDisplay.setGeometry(100, 150, 100, 80)
#btDisplay.resize(200, 100)

win.show()
sys.exit(app.exec_())