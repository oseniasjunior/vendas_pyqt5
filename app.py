import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from forms import MainForm

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)  # enable highdpi scaling
QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)  # use highdpi icons

app = QApplication(sys.argv)

main = MainForm()
main.showMaximized()

sys.exit(app.exec_())
