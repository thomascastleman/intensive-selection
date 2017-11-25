

class Student:

	def __init__(self, _id, _age, _grade, _rank, _isGhost=False):

		self.isGhost = _isGhost
		self.curOfferingID = None	# ID of offering currently paired with this student

		if not self.isGhost:
			self.id = _id			# ID
			self.age = _age			# age of student
			self.grade = _grade		# grade of student (9-12)
			self.rank = _rank		# list of top offerings in prioritized order
			self.gradePriority = [12, 11, 10, 9].index(self.grade) + 1	# 1-4 based on Senior - Freshman

	# for DEBUG
	def log(self):
		print "\nStudent ID: ", self.id
		print "Age: ", self.age
		print "Grade: ", self.grade
		print "Rank: ", self.rank
		print "Priority: ", self.gradePriority
		print "Ghost? ", self.isGhost
		print "Current Offering ID: ", self.curOfferingID