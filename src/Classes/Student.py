

class Student:

	def __init__(self, _id, _age, _grade, _rank, _isGhost=False):

		self.isGhost = _isGhost
		self.curOfferingID = None

		if not self.isGhost:
			self.id = _id			# ID
			self.age = _age			# age of student
			self.grade = _grade		# grade of student (9-12)
			self.rank = _rank		# list of top offerings in prioritized order
			self.gradePriority = [12, 11, 10, 9].index(self.grade) + 1	# 1-4 based on Senior - Freshman