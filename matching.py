
from main import cost

# class to handle a given matching of students to offerings; a given solution
class Matching:

	def __init__(self):
		self.pairs = []
		self.cost = None

	# calculate the cost of an entire matching (sum of the cost of each pair)
	def calcMatchingCost(self):
		self.cost = 0
		for pair in self.pairs:
			self.cost += cost(pair)
		return self.cost