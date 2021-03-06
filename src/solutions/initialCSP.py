"""

Construct an acceptable matching of students to offerings (no age, grade, or capacity violations)
without taking any priority into account,

Modifies student and offering object properties to create pairs
DOES NOT add ghost students

"""

from random import randint, uniform
from ..util import *

# backtracking solution to CSP usable for smaller numbers
def backTrackingSolution(index, students, offerings):

	if index < len(students):
		stu = students[index]	# get student

		for off in offerings:
			# if match found for this student
			if isLegal((stu, off)) and off.curSubscribed < off.maxCapacity:
				stu.curOfferingID = off.id
				off.curSubscribed += 1

				# if rest of solution also adequate
				if backTrackingSolution(index + 1, students, offerings):
					return True
				else:
					off.curSubscribed -= 1

		# if no possible match found, backtrack
		print "Backtracking from index ", index
		return False
	else:
		return True

# solve CSP using min-conflicts -- unnecessary unless data is large
def buildAcceptableSolution(studentList, offeringList, idToStudents, idToOfferings):
	
	netConflict = 0
	alreadyCalculated = [False for i in range(len(studentList))]

	# students cross offerings: holds all static costs calculated for pairs
	stuXoff = [[0 for i in range(len(offeringList))] for j in range(len(studentList))]

	for student in studentList:

		possible = []
		for off in offeringList:
			if isLegal((student, off)) and off.curSubscribed < off.maxCapacity:
				possible.append(off)

		if len(possible) == 0:
			offering = offeringList[randint(0, len(offeringList) - 1)]
		else: 
			offering = possible[randint(0, len(possible) - 1)]
		
		offID = offering.id
		student.curOfferingID = offID

		# update offering's currently subscribed, look for oversubscription
		offering = idToOfferings[offID]
		offering.curSubscribed += 1

		if offering.curSubscribed > offering.maxCapacity:
			offering.capacityCost += 1

		cost = staticCost((student, offering))	# calculate static cost
		stuXoff[student.id][offID] = cost		# store cost value in stuXoff
		offering.pq.put((-cost, student.id))	# add student ID to offering's PQ (negate cost to reverse pq)

		netConflict += cost		# sum all static costs

	# now also add all capacity costs to netconflict
	for offering in offeringList:
		netConflict += offering.capacityCost


	# DEBUG
	print "INITIAL NET CONFLICT:", netConflict

	restartTemp = 100.0
	restartRate = 0.999
	temperature = 100.0
	rate = 0.999 # 0.8

	iterations = 0


	while netConflict > 0:

		# print "Iteration ", iterations, " Temp at ", temperature, " Net conflict == ", netConflict
		
		if uniform(0, 1) > temperature:

			offWithMaxCost = None
			maxCost = None

			# find pair with highest cost
			for offering in offeringList:
				if len(offering.pq.queue) > 0:
					# get first student on offering's PQ
					student = idToStudents[offering.pq.queue[0][1]]
					
					# calculate "true" cost (static cost + oversubscribed cost)
					trueCost = stuXoff[student.id][offering.id] + offering.capacityCost

					# update if new max found
					if maxCost == None or trueCost > maxCost:
						maxCost = trueCost
						offWithMaxCost = offering

			stu = idToStudents[offWithMaxCost.pq.get()[1]]	# get student object

			offWithMinCost = None
			minCost = None



			# find offering that creates pair with lowest cost
			for off in offeringList:
				# calculate static cost if not already stored
				if not alreadyCalculated[stu.id]:
					stuXoff[stu.id][off.id] = staticCost((stu, off))
				# calc true cost
				trueCost = stuXoff[stu.id][off.id] + off.capacityCost
				# update if new min
				if minCost == None or trueCost < minCost:
					minCost = trueCost
					offWithMinCost = off

			alreadyCalculated[stu.id] = True

			# clarifying variable names
			previousOff = offWithMaxCost
			newOff = offWithMinCost

		else:

			# randomize student
			stu = studentList[randint(0, len(studentList) - 1)]

			previousOff = idToOfferings[stu.curOfferingID]

			# remove from pq
			for i in range(0, len(previousOff.pq.queue)):
				ID = previousOff.pq.queue[i][1]
				if ID == stu.id:
					del previousOff.pq.queue[i]
					break

			newOff = offeringList[randint(0, len(offeringList) - 1)]

			# calculated stuXoff values
			if not alreadyCalculated[stu.id]:
				stuXoff[stu.id][previousOff.id] = staticCost((stu, previousOff))
				stuXoff[stu.id][newOff.id] = staticCost((stu, newOff))

		# update attributes of new offering to reflect change
		stu.curOfferingID = newOff.id
		newOff.curSubscribed += 1
		if newOff.curSubscribed > newOff.maxCapacity:
			newOff.capacityCost += 1
			netConflict += 1
		newOff.pq.put((-stuXoff[stu.id][newOff.id], stu.id))

		# update attributes of previous offering to reflect change
		previousOff.curSubscribed -= 1
		if previousOff.capacityCost > 0:
			previousOff.capacityCost -= 1
			netConflict -= 1

		# update net conflict
		netConflict -= stuXoff[stu.id][previousOff.id]
		netConflict += stuXoff[stu.id][newOff.id]

		temperature *= rate

		if temperature < 0.0005: # restartTemp / 4.0:
			temperature = 100.0 # restartTemp
			# restartTemp *= restartRate

			# if restartTemp < 0.0005:
			# 	restartTemp = 100.0
			print "TEMP RESET @ iter=", iterations, " conflict=", netConflict, ", restart=", restartTemp

		iterations += 1


	print "\nPROCESS FINISHED WITH NET CONFLICT: ", netConflict

	valid = testValidity(studentList, offeringList, idToOfferings)
	print "OVERALL VALID? ", valid