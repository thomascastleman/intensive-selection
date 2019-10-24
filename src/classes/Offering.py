# CLASS TO HANDLE ALL DATA FOR EACH OFFERING

import Queue as q

class Offering:

	def __init__(self, _id, _name, _maxCapacity, _minGrade=9, _minAge=0):
		# general use properties:
		self.id = _id
		self.name = _name
		self.maxCapacity = _maxCapacity
		self.minGrade = _minGrade
		self.minAge = _minAge

		# properties for acceptable matching CSP:
		self.curSubscribed = 0	# number of students currently subscribed to this offering
		self.capacityCost = 0	# hard cost when oversubscribed (# of students over capacity)
		self.pq = q.PriorityQueue()	# ID's of currently subscribed students, ordered by static cost

	# FOR DEBUG
	def log(self):
		print "\nOffering ID: ", self.id
		print "Name: ", self.name
		print "Max Cap: ", self.maxCapacity
		print "Min Grade: ", self.minGrade
		print "Min Age: ", self.minAge
		print "Currently Subscribed: ", self.curSubscribed, " students"
		print "Capacity cost: ", self.capacityCost
