
""" GLOBAL VARS: -------------------------------------- """

# number of offerings each student ranks
rankSize = 5

# hashmaps of IDs to objects:
idToOfferings = {}
idToStudents = {}



""" --------------------------------------------------- """

from evaluation import *

def main():
	# from classes.Student import Student
	# test = Student(0, 17, 11, [0, 1, 2, 3, 4])
	# from classes.Offering import Offering
	# off = Offering(0, 20, 11)

	# off.log()
	# test.log()

	# print "success"

	from random import randint
	from classes.Offering import Offering
	from classes.Student import Student

	students = []
	offerings = []

	for i in range(20):
		o = Offering(i, randint(20, 30), randint(9, 12), randint(13, 18))
		offerings.append(o)
		idToOfferings[i] = o

	for i in range(400):
		s = Student(i, randint(13, 18), randint(9, 12), [])

		s.curOfferingID = offerings[randint(0, len(offerings) - 1)].id
		for j in range(0, rankSize):
			s.rank.append(offerings[randint(0, len(offerings) - 1)].id)

		students.append(s)

		idToStudents[i] = s

	evaluate(students, offerings)


	
if __name__ == "__main__":
	main()