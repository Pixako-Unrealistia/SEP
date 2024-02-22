from datetime import date as Date
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QPushButton, QVBoxLayout, QWidget, QLineEdit
from PySide6.QtCore import Qt

class BookingSystem(object):
	def __init__(self):
		self.observers = []
		self.bookings = {}

	def addObserver(self, o):
		self.observers.append(o)

	def notifyObserver(self, data):
		for observer in self.observers:
			observer.update(data)

	def addBooking(self, date, booking):
		if date in self.bookings.keys():
			self.bookings[date].append(booking)
		else:
			self.bookings[date] = [booking]
		self.notifyObserver(self.bookings)

	def getBookings(self, date):
		bookings = []
		for k, v in self.bookings.items():
			if k == date:
				bookings.append(v)
		return bookings

	def display(self, date):
		bookings = self.getBookings(date)
		for booking in bookings:
			print(booking)

class BookingObserver(object):
	def update(self, data):
		pass

class StaffUi(BookingObserver):
	def __init__(self, s, name):
		self.name = name
		self.system = s

	def update(self, bookings):
		print(self.name + ": StaffUi.update():")
		print("-- Booking Data --")
		for date, items in bookings.items():
			for item in items:
				print(str(date) + ": " + item)

	def submit(self, date):
		self.system.display(date)

class BookingList(QMainWindow):
	def __init__(self, staff_ui):
		super().__init__()
		self.staff_ui = staff_ui
		self.setWindowTitle("Booking List")

		self.list_widget = QListWidget()
		self.select_button = QPushButton("Select Booking")

		layout = QVBoxLayout()
		layout.addWidget(self.list_widget)
		layout.addWidget(self.select_button)

		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)

		self.select_button.clicked.connect(self.open_selector)

	def update_list(self, selected_date, bookings):
		self.list_widget.clear()
		for date, items in bookings.items():
			if date == selected_date:
				for item in items:
					self.list_widget.addItem(str(date) + ": " + item)

	def open_selector(self):
		self.booking_selector = BookingSelector(self.staff_ui, self)
		self.booking_selector.show()

class BookingSelector(QMainWindow):
	def __init__(self, staff_ui, booking_list):
		super().__init__()
		self.staff_ui = staff_ui
		self.booking_list = booking_list
		self.setWindowTitle("Booking Selector")

		self.day = QLineEdit()
		self.month = QLineEdit()
		self.year = QLineEdit()
		self.select_button = QPushButton("Submit")

		layout = QVBoxLayout()
		self.day.setPlaceholderText("Day")
		self.month.setPlaceholderText("Month")
		self.year.setPlaceholderText("Year")
		layout.addWidget(self.day)
		layout.addWidget(self.month)
		layout.addWidget(self.year)
		layout.addWidget(self.select_button)

		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)

		self.select_button.clicked.connect(self.submit)

	def submit(self):
		day = int(self.day.text())
		month = int(self.month.text())
		year = int(self.year.text())
		selected_date = Date(year, month, day)
		self.staff_ui.submit(selected_date)
		self.booking_list.update_list(selected_date, self.staff_ui.system.bookings)
		self.close()

s = BookingSystem()


s.addBooking(Date(2011, 9, 1), "Booking#1")
s.addBooking(Date(2011, 10, 1), "Booking#2")
s.addBooking(Date(2011, 10, 1), "Booking#3")
s.addBooking(Date(2011, 11, 1), "Booking#4")
s.addBooking(Date(2011, 12, 1), "Booking#5")

util = StaffUi(s, "UI#1")
s.addObserver(util)


app = QApplication([])
window = BookingList(util)

window.show()
app.exec()
