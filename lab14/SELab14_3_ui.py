import sys
import random
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor
from PySide6.QtWidgets import *



class MainWindow(QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Traffic Light Demo")
		self.setGeometry(100, 100, 300, 100)
		self.target_color = "red"

		self.setup_ui()

	def setup_ui(self):
		layout = QGridLayout()

		self.button_red = QPushButton("")
		self.button_red.clicked.connect(self.flash_red)
		layout.addWidget(self.button_red,0,0)

		self.button_yellow = QPushButton("")
		self.button_yellow.clicked.connect(self.flash_yellow)
		layout.addWidget(self.button_yellow,0,1)

		self.button_green = QPushButton("")
		self.button_green.clicked.connect(self.flash_green)
		layout.addWidget(self.button_green,0,2)

		self.label_number = QLabel("Time: 0")
		layout.addWidget(self.label_number,1,0,1,3)

		self.setLayout(layout)

		self.number = 0
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.update_number)
		self.timer.start(1000)

	def tick(self):
		self.countdown_time -= 1
		print(f"Changing to {self.target_color} in {self.countdown_time}")
		if self.countdown_time <= 0:
			self.countdown_timer.stop()
			self.changeColor(self.target_color)
		

	def changeColor(self, color):
		if color == "red":
			self.flash_red()
		elif color == "yellow":
			self.flash_yellow()
		elif color == "green":
			self.flash_green()


		
	def setTimer(self, duration):
		self.timer = QTimer(self)
		self.timer.setSingleShot(True)
		self.timer.start(duration * 1000)

		# Countdown timer
		self.countdown_timer = QTimer(self)
		self.countdown_timer.timeout.connect(self.tick)
		self.countdown_time = duration
		self.countdown_timer.start(1000)

	def flash_red(self):
		self.button_red.setStyleSheet("background-color: #FF0000")
		self.button_yellow.setStyleSheet("background-color: None")
		self.button_green.setStyleSheet("background-color: None")
		self.target_color = "green"
		self.setTimer(4)
		

	def flash_green(self):
		self.button_red.setStyleSheet("background-color: None")
		self.button_yellow.setStyleSheet("background-color: None")
		self.button_green.setStyleSheet("background-color: #00FF00")
		self.target_color = "yellow"
		self.setTimer(3)

	def flash_yellow(self):
		self.button_red.setStyleSheet("background-color: None")
		self.button_yellow.setStyleSheet("background-color: #FFFF00")
		self.button_green.setStyleSheet("background-color: None")
		self.target_color = "red"
		self.setTimer(2)

	def update_number(self):
		self.number += 1
		self.label_number.setText("Time: {}".format(self.number))


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	window.flash_red()
	sys.exit(app.exec())
