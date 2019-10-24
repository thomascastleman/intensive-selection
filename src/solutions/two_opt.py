# IMPLEMENTATION OF TWO-OPT SOLUTION

from random import randint, uniform
from ..util import *	# access to cost functions / legality checking

# void, updates properties of Student obj 
def two_opt(studentList, offeringList, idToOfferings, logging):

	# calculate age priorities before two-opt
	initAllAgeP(studentList)
	currentCost = getSoftCostOfAllPairs(studentList, idToOfferings)	# calculate soft cost of all pairs
	addAllGhostStudents(studentList, offeringList)	# now add ghosts (since they have no cost)

	if logging: print "Initial Net Cost: {:.3f}".format(currentCost)

	initCost = currentCost

	temp = 100.0	# temperature for simulated annealing
	rate = 0.9999	# rate of temperature decrease
	iteration = 0	# iteration counter
	swaps = 0

	while temp > 0.00001:

		# print "Iteration ", iteration, " temp=", temp, " cost=", currentCost

		# get random pairs
		indA, indB = getRandomIndices(len(studentList))

		studentA = studentList[indA]
		offeringA = idToOfferings[studentA.curOfferingID]

		studentB = studentList[indB]
		offeringB = idToOfferings[studentB.curOfferingID]

		# make swap pairs
		swap1 = (studentA, offeringB)
		swap2 = (studentB, offeringA)

		# if swap is legal
		if isLegal(swap1) and isLegal(swap2):
			# calculate tentative cost as updated by swap
			tentativeCost = currentCost
			tentativeCost -= softCost((studentA, offeringA)) + softCost((studentB, offeringB))
			tentativeCost += softCost(swap1) + softCost(swap2)

			# if swap beneficial OR probabilistic
			if tentativeCost < currentCost or uniform(0, 100) < temp:
				# make swap
				studentA.curOfferingID = offeringB.id
				studentB.curOfferingID = offeringA.id

				currentCost = tentativeCost

				swaps += 1
			
			temp *= rate

		iteration += 1

	if logging:
		print "Finished after %d iterations and %d swaps" % (iteration - 1, swaps)
		print "Net Cost of Final Matching: {:.3f}".format(currentCost)
		print "Net Cost Decrease: {:.3f}".format(initCost - currentCost)

# get two random indices in a matching
def getRandomIndices(numStudents):
	possibleIndices = [i for i in range(numStudents)]

	rand1 = possibleIndices[randint(0, len(possibleIndices) - 1)]
	possibleIndices.remove(rand1)

	rand2 = possibleIndices[randint(0, len(possibleIndices) - 1)]

	return (rand1, rand2)

# sum soft cost across all pairings
def getSoftCostOfAllPairs(students, idToOfferings):
	cost = 0
	for student in students:
		if not student.isGhost:
			offering = idToOfferings[student.curOfferingID]	# get paired offering
			cost += softCost((student, offering))			# add soft cost to total
	return cost

# add necessary ghost students to fill out all empty spots
def addAllGhostStudents(students, offerings):
	from ..classes.Student import Student
	for offering in offerings:
		while offering.curSubscribed < offering.maxCapacity:
			# create new ghost under this offering
			ghost = Student(None, None, None, None, None, None, True)
			ghost.curOfferingID = offering.id
			# add to student list
			students.append(ghost)
			# increase subscription count
			offering.curSubscribed += 1

# remove ghost students
def removeAllGhostStudents(students, idToOfferings):
	newStuList = []
	for stu in students:
		if not stu.isGhost:
			newStuList.append(stu)
		else:
			off = idToOfferings[stu.curOfferingID]
			off.curSubscribed -= 1
	return newStuList