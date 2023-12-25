import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtCore import QTime, QTimer
import random
import os


fileLocation = os.path.dirname(os.path.abspath(__file__))
skillIssue: bool = False
TIME_LIMIT = 30

class Perception_Line:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.w = 0
		self.h = 0
		self.angle = 0
		self.arrow = QPixmap(f"{fileLocation}/images/rabbit.png")
		self.arrow = self.arrow.scaled(self.w, self.h)
		self.arrow = self.arrow.transformed(QTransform().rotate(self.angle))
		
		
	def draw(self, p):
		p.drawPixmap(QRect(self.x, self.y, self.w, self.h), self.arrow)
		
	def set_pos(self, x, y):
		self.x = x
		self.y = y
	
	def set_angle(self, angle):
		self.angle = angle
		self.arrow = self.arrow.transformed(QTransform().rotate(self.angle))
		
	def set_size(self, w, h):
		self.w = w
		self.h = h
		self.arrow = self.arrow.scaled(self.w, self.h)
		self.arrow = self.arrow.transformed(QTransform().rotate(self.angle))
		
	def set_pos_and_angle(self, x, y, angle):
		self.set_pos(x, y)
		self.set_angle(angle)



	
	
	
	

class Predicted_Rabbit:
	def __init__(self):
		self.rabbit = QPixmap(f"{fileLocation}/images/predict_rabbit.png")
		self.current_x = 0
		self.current_y = 0
		self.past_x = 0
		self.past_y = 0
		self.w = 40
		self.h = 40
		
		if skillIssue:
			self.w *= 3
			self.h *= 3
			
	def draw(self, p):
		p.drawPixmap(QRect(self.current_x, self.current_y, self.w, self.h), self.rabbit)
		
	def set_pos(self, x, y):
		self.current_x = x
		self.current_y = y
		
	def random_pos(self, arena_w, arena_h):
		self.past_x = self.current_x
		self.past_y = self.current_y
		self.current_x = random.randint(0, arena_w - self.w)
		self.current_y = random.randint(0, arena_h - self.h)

class Rabbit:
	def __init__(self):
		self.rabbit = QPixmap(f"{fileLocation}/images/rabbit.png")
		self.x = 0
		self.y = 0
		self.w = 40
		self.h = 40

		if skillIssue:
			self.w *= 3
			self.h *= 3

	def draw(self, p):
		p.drawPixmap(QRect(self.x, self.y, self.w, self.h), self.rabbit)

	def random_pos(self, arena_w, arena_h):
		self.x = random.randint(0, arena_w - self.w)
		self.y = random.randint(0, arena_h - self.h)
	
	def set_pos(self, x, y):
		self.x = x
		self.y = y

	def is_hit(self, mouse_x, mouse_y):
		return mouse_x >= self.x and mouse_x <= self.x + self.w and mouse_y >= self.y and mouse_y <= self.y + self.h

class Animation_area(QWidget):
	def __init__(self):
		QWidget.__init__(self, None)
		self.setMinimumSize(300, 300)
		self.arena_w = 300
		self.arena_h = 300
		self.rabbit = Rabbit()
		self.predicted_rabbit = Predicted_Rabbit()
		self.perception_line = Perception_Line()
		self.score = 0
		self.time_limit = TIME_LIMIT
		self.lives = 3
		self.highscore = 0
		
		self.score_label = QLabel(f"Score: {self.score}", self)
		self.score_label.setFont(QFont("Arial", 16))
		self.score_label.move(0, 30)
		self.timer_label = QLabel(f"Time: {self.time_limit}", self)
		self.timer_label.setFont(QFont("Arial", 16))
		self.lives_label = QLabel(f"Lives: {self.lives}", self)
		self.lives_label.setFont(QFont("Arial", 16))
		self.lives_label.move(0, 60)
		
		self.score_label.setFixedWidth(100)
		self.timer_label.setFixedWidth(100)
		self.lives_label.setFixedWidth(100)

		self.game_over_label = QLabel(f"Game Over!\nHighscore:{self.highscore}", self)
		
		self.game_over_label.setFont(QFont("Arial", 30))
		self.game_over_label.move(45, 250)
		self.game_over_label.hide()
		
		self.layout = QVBoxLayout()

		self.speed = 500
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.update_value)
		self.timer.start(self.speed)
		
		self.death_timer = QTimer(self)
		self.death_timer.timeout.connect(self.check_time)
		self.death_timer.start(1000)

		self.QSH = QSoundEffect()
		self.QSH.setSource(QUrl.fromLocalFile(f"{fileLocation}/sounds/rabbit_hit.wav"))
		self.QSM = QSoundEffect()
		self.QSM.setSource(QUrl.fromLocalFile(f"{fileLocation}/sounds/rabbit_missed.wav"))

		self.start_time = QTime.currentTime()

	def mousePressEvent(self, e):
		if not self.game_over_label.isVisible():
			if self.rabbit.is_hit(e.x(), e.y()):
				self.QSH.play()
				self.score += 1
				self.lives += 2
				self.score_label.setText(f"Score: {self.score}")
				self.time_limit += 10
				if self.speed:
					self.speed -= 10
				else:
					self.victory()
				self.timer.start(self.speed)
				self.rabbit.random_pos(self.arena_w, self.arena_h)
				self.update()
				self.update_lives_label()
				self.check_time()
				print(f"Current speed : {self.speed}")
			else:
				self.lives -= 1
				self.QSM.play()
				if self.lives <= 0:
					self.game_over()
				else:
					self.update_lives_label()

	def paintEvent(self, e):
		p = QPainter()
		p.begin(self)
		self.rabbit.draw(p)
		self.predicted_rabbit.draw(p)
		#self.perception_line.draw(p)
		p.end()

	def update_value(self):
		self.predicted_rabbit.random_pos(self.arena_w, self.arena_h)
		self.rabbit.set_pos(self.predicted_rabbit.past_x, self.predicted_rabbit.past_y)
		#self.perception_line.set_pos_and_angle(self.rabbit.x, self.rabbit.y, 0)	
		self.update()
		
	def check_time(self):
		self.time_limit -= 1
		self.timer_label.setText(f"Time: {self.time_limit}")
		if self.time_limit <= 0:
			self.game_over()
	
	def game_over(self):
		self.timer.stop()
		self.death_timer.stop()
		self.timer_label.setText(f"Time: 0")
		self.score_label.setText(f"Score: {self.score}")
		self.lives_label.setText(f"Lives: {self.lives}")
		self.QSM.play()
		self.update()
		if self.score > self.highscore:
			self.highscore = self.score
		
		self.game_over_label.setText(f"Game Over!\nHighscore:{self.highscore}")

		self.game_over_label.show()

		self.restart_button = QPushButton("Restart", self)
		self.restart_button.move(120, 200)
		self.restart_button.show()
		self.restart_button.clicked.connect(self.restart)

	def update_lives_label(self):
		self.lives_label.setText(f"Lives: {self.lives}")
		
	def victory(self):
		self.timer.stop()
		self.death_timer.stop()
		self.timer_label.setText(f"Time: 0")
		self.score_label.setText(f"Score: {self.score}")
		self.lives_label.setText(f"Lives: {self.lives}")
		self.QSM.play()
		self.update()
		self.highscore = self.score

		self.game_over_label.setText("You Win!")
		self.game_over_label.show()

		self.restart_button = QPushButton("Restart", self)
		self.restart_button.move(120, 200)
		self.restart_button.show()
		self.restart_button.clicked.connect(self.restart)
		
		os.system("start https://www.youtube.com/watch?v=dQw4w9WgXcQ")


	def restart(self):
		self.game_over_label.hide()
		self.restart_button.hide()
		self.score = 0
		self.time_limit = TIME_LIMIT
		self.lives = 3
		self.speed = 500
		self.timer.start(self.speed)
		self.score_label.setText(f"Score: {self.score}")
		self.timer_label.setText(f"Time: {self.time_limit}")
		self.lives_label.setText(f"Lives: {self.lives}")
		self.update()

class Simple_animation_window(QWidget):
	def __init__(self):
		QWidget.__init__(self, None)
		self.anim_area = Animation_area()
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.anim_area)
		self.setLayout(self.layout)
		self.setMinimumSize(330, 400)

class StartMenu(QWidget):
	def __init__(self):
		QWidget.__init__(self, None)
		self.setMinimumSize(300, 300)
		self.setWindowTitle("Ultra Rapid Rabbit")
		self.layout = QVBoxLayout()
		self.start_button = QPushButton("Start", self)
		self.start_button.move(120, 200)
		self.start_button.show()
		self.start_button.clicked.connect(self.start)
		self.cheat_button = QPushButton("Cheat", self)
		self.cheat_button.move(120, 250)
		self.cheat_button.show()
		self.cheat_button.clicked.connect(self.cheat)
		self.layout.addWidget(self.start_button)
		self.layout.addWidget(self.cheat_button)
		self.setLayout(self.layout)
		self.setMinimumSize(330, 400)
		
	def cheat(self):
		global skillIssue
		skillIssue = True
		self.start()

	def start(self):
		self.start_button.hide()
		self.cheat_button.hide()
		self.anim_area = Simple_animation_window()
		self.layout.addWidget(self.anim_area)
		self.anim_area.show()

def main():
	app = QApplication(sys.argv)
	w = StartMenu()
	w.show()
	return app.exec_()

if __name__ == "__main__":
	sys.exit(main())
