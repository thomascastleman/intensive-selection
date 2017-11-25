
from random import randrange
from main import *	# access to ID hashmaps
from util import *	# access to cost functions / legality checking
from acceptable_solution import buildAcceptableSolution

# void, updates properties of Student obj 
def two_opt(studentList, offeringList):
	
	buildAcceptableSolution(studentList, offeringList)	# construct initial matching
	currentCost = getSoftCostOfAllPairs(studentList)	# calculate soft cost of all pairs
	addAllGhostStudents(studentList, offeringList)	# now add ghosts (since they have no cost)

	temp = 100.0	# temperature for simulated annealing
	rate = 0.97		# rate of temperature decrease

	while temp > 0.0001:
		# get random pairs
		indA, indB = getRandomIndices(len(studentList))

		studentA = studentList[indA]
		offeringA = idToOffering[studentA.curOfferingID]

		studentB = studentList[indB]
		offeringB = idToOffering[studentB.curOfferingID]

		# make swap pairs
		swap1 = (studentA, offeringB)
		swap2 = (studentB, offeringA)

		# if swap is legal
		if isLegal(swap1) and isLegal(swap2):
			# calculate tentative cost as updated by swap
			tentativeCost = currentCost
			tentativeCost -= (softCost((studentA, offeringA)) + softCost(studentB, offeringB))
			tentativeCost += (softCost(swap1) + softCost(swap2))

			# if swap beneficial OR probabilistic
			if tentativeCost < currentCost or random.randrange(0, 100) < temp:
				# make swap
				studentA.curOfferingID = offeringB.id
				studentB.curOfferingID = offeringA.id
			
			temp *= rate

# get two random indices in a matching
def getRandomIndices(lenOfMatching):
	possibleIndices = [i for i in range(lenOfMatching)]

	rand1 = possibleIndices[randrange(0, len(possibleIndices))]
	possibleIndices.remove(rand1)

	rand2 = possibleIndices[randrange(0, len(possibleIndices))]

	return (rand1, rand2)

# sum soft cost across all pairings
def getSoftCostOfAllPairs(students):
	cost = 0
	for student in students:
		if not student.isGhost:
			offering = idToOffering[student.curOfferingID]	# get paired offering
			cost += softCost((student, offering))			# add soft cost to total
	return cost

# add necessary ghost students to fill out all empty spots
def addAllGhostStudents(students, offerings):
	from classes.Student import Student
	for offering in offerings:
		while offering.curSubscribed < offering.maxCapacity:
			# create new ghost under this offering
			ghost = Student(None, None, None, None, True)
			ghost.curOfferingID = offering.id
			# add to student list
			students.append(ghost)
			# increase subscription count
			offering.curSubscribed += 1