import sys
import os
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect


class Animation_area(QWidget):
	def __init__(self):
		QWidget.__init__(self, None)
		self.paused = False
		self.frame_no = 0
		self.fileDirectory = os.path.dirname(os.path.abspath(__file__))
		self.images = [
			QPixmap(f"{self.fileDirectory}/images/frame-{str(i + 1)}.png") for i in range(20)
			]
		timer = QTimer(self)
		timer.timeout.connect(self.update_value)
		timer.start(75)
		self.QSE = QSoundEffect()
		self.QSE.setSource(QUrl.fromLocalFile(f"{self.fileDirectory}/sounds/rabbit_jump.wav"))
	
	def paintEvent(self, e):
		p = QPainter()
		p.begin(self)
		p.drawPixmap(0, 0, self.images[self.frame_no])
		p.end()
	
	def update_value(self):
		if self.paused:
			return
		self.frame_no += 1
		if self.frame_no >= 20:
			self.frame_no = 0
			self.QSE.play()
		self.update()
	

		


class Simple_animation_window(QWidget):
	def __init__(self):
		QWidget.__init__(self, None)
		self.toggle = False
		self.setWindowTitle("Simple Animation")
		self.anim_area = Animation_area()
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.anim_area)
		self.pauseBtn = QPushButton("Pause")
		self.pauseBtn.clicked.connect(self.pause)
		self.layout.addWidget(self.pauseBtn)
		self.setLayout(self.layout)
		self.setMinimumSize(330, 400)
		
	def pause(self):
		if self.toggle:
			self.anim_area.paused = False
			self.pauseBtn.setText("Pause")
		else:
			self.anim_area.paused = True
			self.pauseBtn.setText("Play")
		self.toggle = not self.toggle
		
	

def main():
	app = QApplication(sys.argv)
	w = Simple_animation_window()
	w.show()
	return app.exec_()

if __name__ == "__main__":
	sys.exit(main())
	