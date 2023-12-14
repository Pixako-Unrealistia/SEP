import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Simple_timer_window(QWidget):
	
	def updateValue(self):
		self.num += 1
		if self.num >= 100:
			self.num = 0
		self.label.setText(str(self.num))
	
	def __init__(self):
		QWidget.__init__(self,None)
		self.num = 0
		vbox = QVBoxLayout()
		self.label = QLabel(self)
		self.label.setText(str(self.num))
		vbox.addWidget(self.label)

		self.timer = QTimer(self)
		self.timer.timeout.connect(self.updateValue)
		self.timer.start(500)

		self.setLayout(vbox)
		self.show()
	

if __name__ == '__main__':
	app = QApplication(sys.argv)
	
	w = Simple_timer_window()
	w.setWindowTitle("Simple")
	w.show()

	sys.exit(app.exec_())
	