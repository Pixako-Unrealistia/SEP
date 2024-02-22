import math
import js
import random
from pyscript import document
from pyodide.ffi import create_proxy

from abc import ABC, abstractmethod

class Villager(ABC):
	def __init__(self, alive):
		self.role = None
		self.display = "?"
		self.alive = alive

	def _is_alive(self):
		return self.alive
	
	def set_display(self, display):
		self.display = display
	
	def _set_alive(self, alive):
		self.alive = alive
	
	def _get_role(self):
		return self.role

	def __str__(self):
		return self.role

class Bearbolf(Villager):
	def __init__(self, alive):
		Villager.__init__(self,  alive)
		self.role = "Bearbolf"


class Rabbit(Villager):
	def __init__(self, alive):
		Villager.__init__(self, alive)
		self.role = "Rabbit"


class Seer(Villager):
	def __init__(self, alive):
		Villager.__init__(self, alive)
		self.role = "Seer"

game = None

class Game:
	def __init__(self):
		
		#CONFIG
		BEAR_COUNT = 2
		RABBIT_COUNT = 8
		SEER_COUNT = 1
		self.villagers = []
		self.gameover = False
		self.consumed = False
		self.player = None # IF ANNOYiNG JUST PUT THIS AS "HI"

		for _ in range(BEAR_COUNT):
			self.villagers.append(Bearbolf(True))
		for _ in range(SEER_COUNT):
			self.villagers.append(Seer(True))
		for _ in range(RABBIT_COUNT):
			self.villagers.append(Rabbit(True))
		random.shuffle(self.villagers)

		self.innocent_list = []
		for i in range(len(self.villagers)):
			if self.villagers[i]._get_role() != "Bearbolf":
				self.innocent_list.append(i)

		self.role_counts = {
			"Seer": 1,
			"Bearbolf": 2,
			"Rabbit": 8,
			"Living" : 10   #TOWNIE ONLY
		}

	def seerPower(self, event):
		if document.getElementById("portrait"):
			document.getElementById("portrait").remove()
		index = int(event.target.id.split("_")[1])
		if self.consumed:
			js.alert("Power has already been used!")
			return
		self.villagers[index].set_display(self.villagers[index]._get_role())


		self.consumed = True
		document.getElementById("villagers").remove()
		self.stop_music()
		self.render()

		announcement = document.createElement("p")
		announcement.innerHTML = f"Seer saw {self.villagers[index]._get_role()}"
		announcement.style.color = "lightblue"
		announcement.style.textShadow = "1px 1px 1px grey"
		document.getElementById("villagers").appendChild(announcement)
		js.Audio.new("./sounds/rabbit_jump.wav").play()

	
	def stop_music(self):
		if self.player:
			self.player.pause()
			self.player.currentTime = 0
	

	def shoot(self, event):
		index = int(event.target.id.split("_")[1])
		death1 = self.kill(index)
		self.consumed = False

		if document.getElementById("portrait"):
			document.getElementById("portrait").remove()

		js.Audio.new("./sounds/rabbit_hit.wav").play()

			


		if not self.gameover:
			death2 = self.bearbolf_kill()
		
		

		if not self.gameover:
			announcement = document.createElement("p")
			announcement.innerHTML = f"Villager no. {death1} got executed!"
			document.getElementById("villagers").appendChild(announcement)
			announcement = document.createElement("p")
			announcement.innerHTML = f"their role was {self.villagers[death1]._get_role()}"
			document.getElementById("villagers").appendChild(announcement)
			announcement = document.createElement("p")
			announcement.innerHTML = f"Villager no. {death2} was slain by the bearbolf!"
			document.getElementById("villagers").appendChild(announcement)
			announcement = document.createElement("p")
			announcement.innerHTML = f"their role was {self.villagers[death2]._get_role()}"
			document.getElementById("villagers").appendChild(announcement)
			announcement = document.createElement("p")
			announcement.innerHTML = f"Living: {self.role_counts['Living']}"
			document.getElementById("villagers").appendChild(announcement)
			announcement = document.createElement("p")
			announcement.innerHTML = f"Bearbolf: {self.role_counts['Bearbolf']}"
			document.getElementById("villagers").appendChild(announcement)
			
			self.stop_music()
			self.player = js.Audio.new("./sounds/daytheme.wav")
			self.player.play()
			self.player.loop = True

			if not self.gameover:
				portrait = document.createElement("img")
				if self.villagers[death1]._get_role() == "Bearbolf":
					portrait.src = "./images/bearbolf.png"
				elif self.villagers[death1]._get_role() == "Seer":
					portrait.src = "./images/seer.png"
				else:
					portrait.src = "./images/rabbit.png"
				portrait.setAttribute("id", "portrait")
				document.getElementById("container").appendChild(portrait)
				document.getElementById("container").appendChild(document.createElement("br"))			
			



	def kill(self, index):
		villager = self.villagers[index]
		villager._set_alive(False)
		villager.set_display(villager._get_role())
		document.getElementById("villagers").remove()
		
		self.role_counts[villager._get_role()] -= 1
		self.role_counts["Living"] -= 1

		self.render()

		if index in self.innocent_list:
			self.innocent_list.remove(index)

		if self.role_counts["Bearbolf"] == 0:
			self.stop_music()
			self.player = js.Audio.new("./sounds/win.mp3")
			self.player.play()
			self.player.loop = True
			document.getElementById("container").innerHTML = "Villagers win!"
			rabbit_widget = AnimationWidget("container")
			rabbit_widget.drawWidget()
			self.gameover = True

		elif self.role_counts["Bearbolf"] >= self.role_counts["Living"]:
			self.stop_music()
			self.player = js.Audio.new("./sounds/lose.mp3")
			self.player.play()
			self.player.loop = True
			document.getElementById("container").innerHTML = "Bearbolfs win!"
			self.gameover = True
			rabbit_widget = AnimationWidget("container")
			rabbit_widget.drawWidget()

		return index

	def bearbolf_kill(self):
		index = random.choice(self.innocent_list)
		print(f"index: {index}")
		self.kill(index)

		return index

	def render(self):
		table = document.createElement("table")
		table.setAttribute("id", "villagers")
		document.getElementById("container").appendChild(table)
		
		header = table.createTHead()
		headerRow = header.insertRow(0)
		headerRow.insertCell(0).innerHTML = "Role"
		headerRow.insertCell(1).innerHTML = "Alive"
		headerRow.insertCell(2).innerHTML = "Ability"
		
		body = table.createTBody()
		for i in range(len(self.villagers)):
			row = body.insertRow(i)
			#if alive, mark role as ?
			#else, mark role as the role
			alive = self.villagers[i]._is_alive()
			if not alive:			
				row.insertCell(0).innerHTML = self.villagers[i]._get_role()
				row.insertCell(1).innerHTML = str(self.villagers[i]._is_alive())
			else:
				row.insertCell(0).innerHTML = self.villagers[i].display
				row.insertCell(1).innerHTML = str(self.villagers[i]._is_alive())
				button = document.createElement("button")
				button.innerHTML = "Shoot"
				button.setAttribute("id", f"shoot_{i}")
				button.onclick = self.shoot
				row.insertCell(2).appendChild(button)

				if self.role_counts["Seer"] > 0 and not self.consumed:
					button = document.createElement("button")
					button.innerHTML = "Seer Power"
					button.setAttribute("id", f"seer_{i}")
					button.onclick = self.seerPower
					row.insertCell(2).appendChild(button)
		

# To sastisfy requirement
					

class AbstractWidget(ABC):
	def __init__(self, element_id):
		self.element_id = element_id
		self._element = None

	@property
	def element(self):
		if not self._element:
			self._element = document.getElementById(self.element_id)
		return self._element
	
	@abstractmethod
	def drawWidget(self):
		pass

class AnimationWidget(AbstractWidget):
	def __init__(self, element_id):
		AbstractWidget.__init__(self, element_id)
		self.counter = 1

	def on_click(self, event):
		self.counter += 1
		self.element.innerText = f"Hello {self.counter}"

	def on_setInterval(self):
		self.counter += 5
		if self.counter > 20:
			self.counter = 1
		self.image.src = f"./images/frame-{self.counter}.png"

class AnimationWidget(AbstractWidget):
	def __init__(self, element_id):
		AbstractWidget.__init__(self, element_id)
		self.counter = 1

	def on_click(self, event):
		js.location.reload()

	def on_setInterval(self):
		self.counter += 1
		if self.counter > 20:
			self.counter = 1
		self.image.src = f"./images/frame-{self.counter}.png"

	def drawWidget(self):
		self.image = document.createElement("img")
		self.image.style.width = "600px"
		self.image.style.height = "600px"
		self.image.src = f"./images/frame-1.png"
		on_setInterval = create_proxy(self.on_setInterval)
		js.setInterval(on_setInterval, 100)
		self.element.appendChild(self.image)
		self.jump_sound = js.Audio.new("./sounds/rabbit_jump.wav")
		self.button = document.createElement("button")
		self.button.innerText = "newgame"
		self.button.style.width = "600px"
		self.button.onclick = self.on_click
		self.element.appendChild(self.button)					
		
if __name__ == "__main__":
	game = Game()
	game.render()
