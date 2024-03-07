
class University():
	def __init__(self, name, programs):
		self.name = name
		self.program = [Program]
		self.student = {} #key = ID, value = Student
	
class Program():
	def __init__(self, level :str, name : str, start : str, courses : [Course]):
		self.level = level
		self.name = name
		self.start = start
		self.courses = courses

	def addCourse(self, Course):
		pass

	def getCourse(self, Course):
		pass

class Course():
	def __init__(self, credit : int, id : int, lecturer : Lecturer, name : str, semester : str, student_list : [Student]):
		self.credit = credit
		self.id = id
		self.lecturer = lecturer
		self.name = name
		self.semester = semester
		self.student_list = student_list

	def enroll(self, name : str):
		pass

	def getCredit(self):
		pass

	def getLecturer(self):
		pass

	def getStudents(self):
		pass

class Lecturer():
	def __init__(self, name : str, id : int, course_list : [Course]):
		self.name = name
		self.id = id
		self.course_list = course_list

	def getCourse(self, Course):
		pass


class Student():
	def __init__(self, id : int, name : str, course_list : [Course]):
		self.name = name
		self.id = id
		self.status = "normal"
		self.course_list = course_list

class Take():
	def __init__(self, grade : str, scores : int, student : Student, course : Course):
		self.grade = grade
		self.scores = scores
		self.student = student
		self.course = course

	
class Transcript ():
	def __init__(self, complete : bool, issue_date : str, take_list : [Take]):
		self.complete = complete
		self.issue_date = issue_date
		self.take_list = take_list
	
	def printTranscript(self):
		pass