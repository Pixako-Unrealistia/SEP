import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from homework import Ui_Form 
from homework import Ui_alert

class Alert(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_alert()
		self.ui.setupUi(self)
		self.ui.okay.clicked.connect(self.snooze)
		self.ui.pushButton_2.clicked.connect(self.okay)
    
	def snooze(self):
		self.close()
		self.window = Timer()
		self.window.show()
    
	def okay(self):
		self.close()

class Timer(QMainWindow):

	def __init__(self):
		super().__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.ui.setTime.clicked.connect(self.set)
		self.ui.resetTime.clicked.connect(self.reset)
		self.timer = QTimer()
		self.timer.timeout.connect(self.update)
		self.timer.isActive = False
		self.time = 0
		self.ui.label.setText(f"Set timer")
		self.ui.label.adjustSize()
		self.ui.oneMin.clicked.connect(self.one)
		self.ui.fiveMin.clicked.connect(self.five)
		self.ui.tenMin.clicked.connect(self.ten)
		self.ui.snooze.clicked.connect(self.snooze)
		

	def set(self):
		self.time = int(self.ui.textEdit_2.toPlainText())
		self.timer.start(1000)
		self.timer.isActive = True
		self.ui.label.setText(f"Time left: {self.time}")
		self.ui.label.adjustSize()

	def reset(self):
		self.time = 0
		self.ui.label.setText(f"Set timer")
		self.ui.label.adjustSize()
		self.timer.stop()
		self.timer.isActive = False

	def update(self):
		if self.time > 0:
			self.time -= 1
			self.ui.label.setText(f"Time left: {self.time}")
			self.ui.label.adjustSize()
		else:
			self.timer.stop()
			self.timer.isActive = False
			self.close()
			self.window = Alert()
			self.window.show()
	
	def one(self):
		self.time = 60
		self.timer.start(1000)
		self.timer.isActive = True
		self.ui.label.setText(f"Time left: {self.time}")
		self.ui.label.adjustSize()

	def five(self):
		self.time = 300
		self.timer.start(1000)
		self.timer.isActive = True
		self.ui.label.setText(f"Time left: {self.time}")
		self.ui.label.adjustSize()

	def ten(self):
		self.time = 600
		self.timer.start(1000)
		self.timer.isActive = True
		self.ui.label.setText(f"Time left: {self.time}")
		self.ui.label.adjustSize()
		
	def snooze(self):
		#add more time from input
		self.time += int(self.ui.textEdit_2.toPlainText())
		self.timer.start(1000)
		self.timer.isActive = True
		self.ui.label.setText(f"Time left: {self.time}")
		self.ui.label.adjustSize()




if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Timer()
	window.show()
	sys.exit(app.exec_())