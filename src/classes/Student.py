# CLASS TO HANDLE ALL DATA FOR EACH STUDENT

class Student:

	def __init__(self, _id, _email, _name, _age, _grade, _rank=[], _isGhost=False):

		self.isGhost = _isGhost
		self.curOfferingID = None	# ID of offering currently paired with this student

		if not self.isGhost:
			self.id = _id			# ID
			self.email = _email
			self.name = _name
			self.age = _age			# age of student
			self.grade = _grade		# grade of student (9-12)
			self.rank = _rank		# list of top offerings in prioritized order

			# grade priority: in range (0, 1), equal to student's inverse grade value (1-4 for 12-9) over num possible grades (4)
			self.gradeP = ([12, 11, 10, 9].index(self.grade) + 1) / 4.0
			# age priority: in range (0, 1), equal to inverse age value relative to age range, (1-n, max-min) over age range
			self.ageP = 0.0

	# for DEBUG
	def log(self):
		print "\nStudent ID: ", self.id
		print "Email: ", self.email
		print "Name: ", self.name
		print "Age: ", self.age
		print "Grade: ", self.grade
		print "Rank: ", self.rank
		print "Grade Priority: ", self.gradeP
		print "Age Priority: ", self.ageP
		print "Ghost? ", self.isGhost
		print "Current Offering ID: ", self.curOfferingID