import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from program3_1 import Ui_Form

def say_hello():
    print("Hello World!")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    ui.pushButton.clicked.connect(say_hello)
    widget.show()
    sys.exit(app.exec_())
