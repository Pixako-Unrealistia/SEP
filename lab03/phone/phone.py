import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from program3_3 import Ui_Form

class Phone(QMainWindow):

		
		def one(self):
			self.num += "1"
			self.ui.lineEdit.setText(self.num)

		def	two(self):
			self.num+= "2"
			self.ui.lineEdit.setText(self.num)
			
		def three(self):
			self.num += "3"
			self.ui.lineEdit.setText(self.num)

		def four(self):
			self.num += "4"
			self.ui.lineEdit.setText(self.num)
	
		def five(self):
			self.num += "5"
			self.ui.lineEdit.setText(self.num)
	
		def six(self):
			self.num += "6"
			self.ui.lineEdit.setText(self.num)

		def seven(self):
			self.num += "7"
			self.ui.lineEdit.setText(self.num)

		def eight(self):
			self.num += "8"
			self.ui.lineEdit.setText(self.num)
	
		def nine(self):
			self.num += "9"
			self.ui.lineEdit.setText(self.num)

		def star(self):
			self.num += "*"
			self.ui.lineEdit.setText(self.num)
	
		def zero(self):
			self.num += "0"
			self.ui.lineEdit.setText(self.num)

		def sharp(self):
			self.num += "#"
			self.ui.lineEdit.setText(self.num)

		def call(self):
			self.call = QMessageBox()
			self.call.setText(f"Dialing {self.num}")
			self.call.exec_()
			
	
		def back(self):
			self.num = self.num[:-1]
			self.ui.lineEdit.setText(self.num)

		def __init__(self):
			QMainWindow.__init__(self, None)
			self.ui = Ui_Form()
			self.ui.setupUi(self)
			self.num = ""
			self.ui.b_1.clicked.connect(self.one)
			self.ui.b_2.clicked.connect(self.two)
			self.ui.b_3.clicked.connect(self.three)
			self.ui.b_4.clicked.connect(self.four)
			self.ui.b_5.clicked.connect(self.five)
			self.ui.b_6.clicked.connect(self.six)
			self.ui.b_7.clicked.connect(self.seven)
			self.ui.b_8.clicked.connect(self.eight)
			self.ui.b_9.clicked.connect(self.nine)
			self.ui.b_10.clicked.connect(self.star)
			self.ui.b_11.clicked.connect(self.zero)
			self.ui.b_12.clicked.connect(self.sharp)
			self.ui.b_13.clicked.connect(self.call)
			self.ui.b_14.clicked.connect(self.back)
			self.ui.lineEdit.setText(self.num)
			

			

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = Phone()
	widget.show()
	sys.exit(app.exec_())


		