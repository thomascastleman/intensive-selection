
from main import *

def two_opt(studentList, offeringList):
	pass


# calculate the cost of a single pair, of the form (student, offering)
def cost(pair):
	student, offering = pair

	if offering.id not in student.rank:
		rankPriority = rankSize + 1
	else:
		rankPriority = student.rank.index(offering.id) + 1

	return rankPriority + student.gradePriority

# determine if a pairing is legal based on grade / age restrictions
def isLegal(pair):
	student, offering = pair
	return student.grade < offering.minGrade or student.age < offering.minAge: