import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import datetime


class Simple_timer_window(QWidget):

	def updateValue(self):
		self.label.setText(str(datetime.datetime.now().strftime("%X")))
		self.label.adjustSize()
	
	def __init__(self):
		QWidget.__init__(self,None)
		self.start_time = datetime.datetime.now()
		
		vbox = QVBoxLayout()
		self.label = QLabel(self)
		self.label.setText(str(self.start_time))
		vbox.addWidget(self.label)

		self.timer = QTimer(self)
		self.timer.timeout.connect(self.updateValue)
		self.timer.start(1)

		self.setLayout(vbox)
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	
	w = Simple_timer_window()
	w.setWindowTitle("Timer")
	w.show()

	sys.exit(app.exec_())
	