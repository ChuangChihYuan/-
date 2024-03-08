import sys
from PySide6 import QtWidgets as qtw
from controller import *


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
