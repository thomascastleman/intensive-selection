

class Student:

	def __init__(self, _rank, _age, _grade, _isGhost=False):

		self.isGhost = _isGhost

		if not self.isGhost:
			self.rank = _rank											# list of top offerings in prioritized order
			self.age = _age												# age of student
			self.grade = _grade											# grade of student (9-12)
			self.gradePriority = [12, 11, 10, 9].index(self.grade) + 1	# 1-4 based on Senior - Freshman
