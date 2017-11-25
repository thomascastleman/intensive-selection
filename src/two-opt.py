
import random
from main import *
from acceptable_solution import buildAcceptableSolution

# returns Matching object
def two_opt(studentList, offeringList):
	
	matching = buildAcceptableSolution(studentList, offeringList)	# construct initial matching
	currentCost = matching.calcMatchingCost(softCost)				# calculate cost of that matching

	temp = 100.0	# temperature for simulated annealing
	rate = 0.97		# rate of temperature decrease

	while temp > 0.0001:
		# get random pairs from matching
		indA, indB = getRandomIndices(len(matching.pairs))
		studentA, offeringA = matching.pairs[indA]
		studentB, offeringB = matching.pairs[indB]

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
				# remove both previous pairs
				del matching.pairs[indA]
				del matching.pairs[indB]
				# add swapped pairs
				matching.pairs.append(swap1)
				matching.pairs.append(swap2)
			
			temp *= rate

	return matching

# get two random indices in a matching
def getRandomIndices(lenOfMatching):
	possibleIndices = [i for i in range(lenOfMatching)]

	rand1 = possibleIndices[random.randrange(0, len(possibleIndices))]
	possibleIndices.remove(rand1)

	rand2 = possibleIndices[random.randrange(0, len(possibleIndices))]

	return (rand1, rand2)