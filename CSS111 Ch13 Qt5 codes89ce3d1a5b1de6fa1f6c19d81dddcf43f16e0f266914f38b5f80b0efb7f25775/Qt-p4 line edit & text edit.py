from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
win = QMainWindow()
win.setWindowTitle("Main Window")
win.setGeometry(400, 400, 500, 500)

line = QLineEdit(win)
line.setText('Hello')
line.move(20, 80)

def show():
    print('[' + line.text() + ']')

btSubmit = QPushButton(win)
btSubmit.setText("Submit")
btSubmit.clicked.connect(show)
btSubmit.move(20, 150)

btClear = QPushButton(win)
btClear.setText("Clear")
btClear.clicked.connect(line.clear)
btClear.move(20, 220)

teBox = QTextEdit(win)
teBox.setGeometry(150, 50, 300, 400)
teBox.setText('This is QTextEdit')

win.show()
sys.exit(app.exec_())