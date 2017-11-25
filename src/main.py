
rankSize = 5		# number of offerings each student ranks

# hashmaps of IDs to objects:
idToOfferings = {}
idToStudents = {}

def main():
	from classes.Student import Student
	test = Student(0, 17, 11, [0, 1, 2, 3, 4])
	from classes.Offering import Offering
	off = Offering(0, 20, 11)

	off.log()
	test.log()

	print "success"


main()