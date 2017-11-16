
from main import *

# construct an initial randomized but legal matching
def buildInitialMatching(studentList, offeringList):
	pass

# returns list of tuple pairs of (student, offering)
def two_opt(studentList, offeringList):
	pass


# calculate the cost of a single pair, of the form (student, offering)
def cost(pair):
	student, offering = pair

	if student.isGhost:
		return 0
	else:
		if offering.id not in student.rank:
			rankPriority = rankSize + 1		# if offering not on rank, default to 1 more than size of rank
		else:
			rankPriority = student.rank.index(offering.id) + 1	# use position of offering on student's rank

		return rankPriority + student.gradePriority

# determine if a pairing is legal based on grade / age restrictions
def isLegal(pair):
	student, offering = pair
	return student.isGhost or (student.grade >= offering.minGrade and student.age >= offering.minAge)