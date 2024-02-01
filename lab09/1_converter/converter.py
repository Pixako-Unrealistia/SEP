import js
from pyscript import document
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
        pass

class CurrencyConverterWidget(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)

    def on_click_thb_to_usd(self, event):
        thb_amount = float(self.input_text_thb.value)
        usd_amount = thb_amount / 30
        js.alert(f"{thb_amount} THB == {usd_amount} USD")

    def on_click_usd_to_thb(self, event):
        usd_amount = float(self.input_text_usd.value)
        thb_amount = usd_amount * 30
        js.alert(f"{usd_amount} USD == {thb_amount} THB")

    def drawWidget(self):
        self.input_text_thb = document.createElement("input", type="text")
        self.input_text_thb.style.width = "600px"
        self.element.appendChild(self.input_text_thb)

        self.button_thb_to_usd = document.createElement("button")
        self.button_thb_to_usd.innerText = "Convert THB to USD"
        self.button_thb_to_usd.style.width = "600px"
        self.button_thb_to_usd.onclick = self.on_click_thb_to_usd
        self.element.appendChild(self.button_thb_to_usd)

        self.input_text_usd = document.createElement("input", type="text")
        self.input_text_usd.style.width = "600px"
        self.element.appendChild(self.input_text_usd)

        self.button_usd_to_thb = document.createElement("button")
        self.button_usd_to_thb.innerText = "Convert USD to THB"
        self.button_usd_to_thb.style.width = "600px"
        self.button_usd_to_thb.onclick = self.on_click_usd_to_thb
        self.element.appendChild(self.button_usd_to_thb)

if __name__ == "__main__":
    converter = CurrencyConverterWidget("container")
    converter.drawWidget()