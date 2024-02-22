import js
from pyscript import document
from pyodide.ffi import create_proxy

from abc import ABC, abstractmethod

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
		self.div = document.createElement("div")
		self.element.appendChild(self.div)

class AnimationWidget(AbstractWidget):
	def __init__(self, element_id):
		AbstractWidget.__init__(self, element_id)
		self.counter = 1

	def on_click(self, event):
		self.counter += 1
		self.element.innerText = f"Hello {self.counter}"

	def on_setInterval(self):
		self.counter += 1
		if self.counter > 20:
			self.counter = 1
		self.image.src = f"./images/frame-{self.counter}.png"

class AnimationWidget(AbstractWidget):
	def __init__(self, element_id):
		AbstractWidget.__init__(self, element_id)
		self.counter = 1
		self.is_paused = False

	def on_click(self, event):
		self.is_paused = not self.is_paused
		self.button.innerText = "Resume" if self.is_paused else "Pause"

	def on_setInterval(self):
		if not self.is_paused:
			self.counter += 1
			if self.counter > 20:
				self.counter = 1
			self.image.src = f"./images/frame-{self.counter}.png"

	def drawWidget(self):
		self.div = document.createElement("div")
		super().drawWidget()
		self.image = document.createElement("img")
		self.image.style.width = "600px"
		self.image.style.height = "600px"
		self.image.src = f"./images/frame-1.png"
		on_setInterval = create_proxy(self.on_setInterval)
		js.setInterval(on_setInterval, 100)
		self.div.appendChild(self.image)
		self.jump_sound = js.Audio.new("./sounds/rabbit_jump.wav")
		self.button = document.createElement("button")
		self.button.innerText = "Pause"
		self.button.style.width = "600px"
		self.button.onclick = self.on_click
		self.div.appendChild(self.button)
		self.element.appendChild(self.div)


class ColorfulAnimationWidget(AnimationWidget):
	def __init__(self, element_id):
		AnimationWidget.__init__(self, element_id)

	def color_click(self, event):
		self.div.style.backgroundColor = f"rgb({js.Math.random()*255},{js.Math.random()*255},{js.Math.random()*255})"

	def drawWidget(self):
		self.div = document.createElement("div")
		super().drawWidget()
		self.color_button = document.createElement("button")
		self.color_button.innerText = "Change Color"
		self.color_button.style.width = "600px"
		self.color_button.onclick = self.color_click
		self.div.appendChild(self.color_button)
		self.element.appendChild(self.div)


class AbstractContainer(ABC):
	def __init__(self, element_id):
		self.widgets = []
		self.element_id = element_id
		self._element = None

	@property
	def element(self):
		if not self._element:
			self._element = document.getElementById(self.element_id)
		return self._element

	def addWidget(self, widget):
		self.widgets.append(widget)
		widget.drawWidget()

	@abstractmethod
	def drawWidgets(self):
		pass

	def createWidgetButton(self, widget_class, button_text):
		button = document.createElement("button")
		button.innerText = button_text
		button.onclick = lambda event: self.addWidget(widget_class(self.element_id))
		self.element.appendChild(button)


class WidgetContainer(AbstractContainer):
	def drawWidgets(self):
		for widget in self.widgets:
			widget.drawWidget()


if __name__ == "__main__":
	container = WidgetContainer("container")
	container.createWidgetButton(AnimationWidget, "Add Animation Widget")
	container.createWidgetButton(ColorfulAnimationWidget, "Add Colorful Animation Widget")