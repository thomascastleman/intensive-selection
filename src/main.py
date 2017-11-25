
rankSize = 5		# number of offerings each student ranks

# hashmaps of IDs to objects:
idToOfferings = {}
idToStudents = {}

# calculate cost of a pair with respect to PRIORITIES
def softCost(pair):
	student, offering = pair

	if student.isGhost:
		return 0
	else:
		if offering.id not in student.rank:
			rankPriority = rankSize + 1		# if offering not on rank, default to 1 more than size of rank
		else:
			rankPriority = student.rank.index(offering.id) + 1	# use position of offering on student's rank

		return rankPriority + student.gradePriority

# calculate cost of a pair with respect to the age / grade HARD CONSTRAINTS
def staticCost(pair):
	student, offering = pair
	return (1 if student.age < offering.minAge else 0) + (1 if student.grade < offering.minGrade else 0)


# determine if a pair is legal based on grade / age restrictions
def isLegal(pair):
	student, offering = pair
	return student.isGhost or (student.grade >= offering.minGrade and student.age >= offering.minAge)


def main():
	from classes.Student import Student
	test = Student(0, 17, 11, [0, 1, 2, 3, 4])
	from classes.Offering import Offering
	off = Offering(0, 20, 11)

	off.log()
	test.log()

	print "success"


main()