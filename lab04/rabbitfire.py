import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect
import random
import os 

fileLocation = os.path.dirname(os.path.abspath(__file__))
skillIssue : bool = False
class Rabbit:
	def __init__(self):
		self.rabbit = QPixmap(f"{fileLocation}/images/rabbit.png")
		self.x = 0
		self.y = 0
		self.w = 40
		self.h = 40
		
		if (skillIssue == True):
			self.w *= 4
			self.h *= 4

	def draw(self, p):
		p.drawPixmap(QRect(self.x, self.y, self.w, self.h), self.rabbit)
	
	def random_pos(self, arena_w, arena_h):
		self.x = random.randint(0, arena_w - self.w)
		self.y = random.randint(0, arena_h - self.h)
   
	def is_hit(self, mouse_x, mouse_y):
		return mouse_x >= self.x and mouse_x <= self.x + self.w and mouse_y >= self.y and mouse_y <= self.y + self.h
	
class Animation_area(QWidget):
	def __init__(self):
		QWidget.__init__(self, None)
		self.setMinimumSize(300, 300)
		self.arena_w = 300
		self.arena_h = 300
		self.rabbit = Rabbit()
		timer = QTimer(self)
		timer.timeout.connect(self.update_value)
		timer.start(500)
		self.QSH = QSoundEffect()
		self.QSH.setSource(QUrl.fromLocalFile(f"{fileLocation}/sounds/rabbit_hit.wav"))
		self.QSM = QSoundEffect()
		self.QSM.setSource(QUrl.fromLocalFile(f"{fileLocation}/sounds/rabbit_missed.wav"))
		
		
	def mousePressEvent(self, e):
		if self.rabbit.is_hit(e.x(), e.y()):
			print("Hit!!!")
			self.QSH.play()
		else:
			print("Missed!!!")
			self.QSM.play()
			

	def paintEvent(self, e):
		p = QPainter()
		p.begin(self)
		self.rabbit.draw(p)
		p.end()

	def update_value(self):
		self.rabbit.random_pos(self.arena_w, self.arena_h)
		self.update()

class Simple_animation_window(QWidget):
	def __init__(self):
		QWidget.__init__(self, None)
		self.anim_area = Animation_area()
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.anim_area)
		self.setLayout(self.layout)
		self.setMinimumSize(330, 400)
		
def main():
	app = QApplication(sys.argv)
	w = Simple_animation_window()
	w.show()
	return app.exec_()

if __name__ == "__main__":
	sys.exit(main())