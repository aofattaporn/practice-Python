#from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
win = QMainWindow()
win.setWindowTitle("CheckedBox")
win.setGeometry(400, 400, 500, 200)

# a label
#
label = QLabel(win)
label.setText("Please try clicking the button.")
label.adjustSize()
label.move(20, 30)

# a checkbox
#
def show():
    print(check.text())
    print(check.checkState())
    if check.isChecked():
        label.setText("Checked.")
    else:
        label.setText("Unchecked.")

check = QCheckBox(win)
check.setText("Option1")
check.move(20, 80)
check.stateChanged.connect(show)

win.show()
sys.exit(app.exec_())