
""" GLOBAL VARS: -------------------------------------- """

# number of offerings each student ranks
rankSize = 5

# hashmaps of IDs to objects:
idToOfferings = {}
idToStudents = {}



""" --------------------------------------------------- """

from evaluation import *

def main():

	# EXTREMELY UNREASONABLE TEST DATA: (FOR EVAL TESTING)

	# from random import randint
	# from classes.Offering import Offering
	# from classes.Student import Student

	# students = []
	# offerings = []

	# for i in range(20):
	# 	o = Offering(i, randint(20, 30), randint(9, 12), randint(13, 18))
	# 	offerings.append(o)
	# 	idToOfferings[i] = o

	# for i in range(400):
	# 	s = Student(i, randint(13, 18), randint(9, 12), [])

	# 	off = offerings[randint(0, len(offerings) - 1)]
	# 	s.curOfferingID = off.id
	# 	off.curSubscribed += 1



	# 	for j in range(0, rankSize):
	# 		s.rank.append(offerings[randint(0, len(offerings) - 1)].id)

	# 	students.append(s)

	# 	idToStudents[i] = s

	# evaluate(students, offerings)


	
if __name__ == "__main__":
	main()