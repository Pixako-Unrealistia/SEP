class Time:
	def __init__(self, hour : int, minute : int, second:int):
		self.hour = str(hour).zfill(2)
		self.minute = str(minute).zfill(2)
		self.second = str(second).zfill(2)
	
	def __str__(self):
		return f"{self.hour}:{self.minute}:{self.second} Hrs."

	def print(self):
		print(self)

	def set(self, hour, minute, second):
		self.hour = str(hour).zfill(2)
		self.minute = str(minute).zfill(2)
		self.second = str(second).zfill(2)

	def get(self): #not specified what to return so tuple...?
		return ((self.hour, self.minute, self.second))


time1 = Time(9,39,0)
time1.print()
print(time1.get())

print("\n\nAssigned new time:")
time1.set(10, 45, 30)
time1.print()
print(time1.get())