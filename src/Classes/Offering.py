

class Offering:

	def __init__(self, _id, _maxCapacity, _minGrade=9, _minAge=0):

		self.id = _id
		self.maxCapacity = _maxCapacity
		self.minGrade = _minGrade
		self.minAge = _minAge

		self.curSubscribed = 0	# number of students currently subscribed to this offering
		self.capacityCost = 0	# hard cost when oversubscribed (# of students over capacity)