import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class THB_converter(QWidget):
	def convert(self):
		amount = float(self.entry.text())
		self.label.setText(str(amount*30.0))
		self.label.adjustSize()

	def __init__(self):
		QWidget.__init__(self,None)
		self.setWindowTitle("THB Converter")
		vbox = QVBoxLayout()
		self.label = QLabel(self)
		self.label.setText("THB")
		vbox.addWidget(self.label)

		self.entry = QLineEdit(self)
		self.entry.setText("0")
		vbox.addWidget(self.entry)

		self.button = QPushButton("Convert",self)
		self.button.clicked.connect(self.convert)
		vbox.addWidget(self.button)

		self.setLayout(vbox)
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	
	w = THB_converter()
	w.setWindowTitle("THB Converter")
	w.show()

	sys.exit(app.exec_())

