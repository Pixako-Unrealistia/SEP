import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *


class popup(QWidget):
	def __init__(self):
		QWidget.__init__(self,None)
		vbox = QVBoxLayout()
		self.label = QLabel(self)
		self.label.setText("Time's up")
		vbox.addWidget(self.label)

		self.btn = QPushButton('Close', self)
		self.btn.clicked.connect(self.close)
		vbox.addWidget(self.btn)

		self.setLayout(vbox)
		self.show()
	
class Alarm(QWidget):
	
	def updateAlarm(self):
		try:
			time_value = int(self.time.text())
			if time_value <= 0:
				raise ValueError("Time must be a positive number")
		except ValueError as e:
			self.label.setText(str(e))
			return

		self.time.setDisabled(True)
		self.btn.setDisabled(True)
		self.label.setText("Alarm set to " + self.time.text() + " seconds")
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.updateValue)
		self.timer.start(time_value * 1000)
		self.remaining_time = time_value
		self.countdown_timer = QTimer(self)
		self.countdown_timer.timeout.connect(self.updateCountdown)
		self.countdown_timer.start(1000)

	def updateCountdown(self):
		self.remaining_time -= 1
		self.label.setText("Time remaining: " + str(self.remaining_time) + " seconds")
		if self.remaining_time <= 0:
			self.countdown_timer.stop()
			self.popup = popup()
			self.popup.setWindowTitle("Time's up")
			self.popup.show()
			self.timer.stop()
			self.label.setText("Alarm")
			self.time.setText("Enter how many seconds")
			self.time.setDisabled(False)
			self.btn.setDisabled(False)
			

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
