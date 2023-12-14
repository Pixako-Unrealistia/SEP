import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Alarm(QWidget):
	
	def updateAlarm(self):
		self.label.setText("Alarm set to " + self.time.text() + " seconds")
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.updateValue)
		self.timer.start(int(self.time.text()) * 1000)
		self.remaining_time = int(self.time.text())
		self.countdown_timer = QTimer(self)
		self.countdown_timer.timeout.connect(self.updateCountdown)
		self.countdown_timer.start(1000)

	def updateCountdown(self):
		self.remaining_time -= 1
		self.label.setText("Time remaining: " + str(self.remaining_time) + " seconds")
		if self.remaining_time <= 0:
			self.countdown_timer.stop()
			self.label.setText("Time's up!")

	def updateValue(self):
		self.label.setText("Alarm")
		self.timer.stop()
	
	def __init__(self):
		QWidget.__init__(self,None)
		vbox = QVBoxLayout()
		self.label = QLabel(self)
		self.label.setText("Alarm")
		vbox.addWidget(self.label)

		self.time = QLineEdit(self)
		self.time.setText("Enter how many seconds")
		vbox.addWidget(self.time)

		self.btn = QPushButton('Set alarm', self)
		self.btn.clicked.connect(self.updateAlarm)
		vbox.addWidget(self.btn)

		self.setLayout(vbox)
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	
	w = Alarm()
	w.setWindowTitle("Set alarm")
	w.show()

	sys.exit(app.exec_())
