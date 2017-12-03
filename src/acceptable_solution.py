"""

Construct an acceptable matching of students to offerings (no age, grade, or capacity violations)
without taking any priority into account,
using minimum conflicts alg with simulated annealing

Receives lists of Student and Offering objects
Modifies student and offering properties to create pairs
DOES NOT add ghost students

"""

from random import randint, uniform
from util import *

def buildAcceptableSolution(studentList, offeringList, idToStudents, idToOfferings):
	
	netConflict = 0
	alreadyCalculated = [False for i in range(len(studentList))]

	# students cross offerings: holds all static costs calculated for pairs
	stuXoff = [[0 for i in range(len(offeringList))] for j in range(len(studentList))]


	for student in studentList:
		# randomize offering
		offID = randint(0, len(offeringList) - 1)
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
	print "INITIAL NET CONFLICT: ", netConflict

	# print "STUXOFF: "
	# for row in stuXoff:
	# 	print row

	temperature = 100.0
	rate = 0.99
	iterations = 0


	while netConflict > 0:

		print "Iteration ", iterations, " Temp at ", temperature
		
		if uniform(0, 1) > temperature:

			offWithMaxCost = None
			maxCost = None

			# find pair with highest cost
			for offering in offeringList:
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



		print "Previous true cost: ", stuXoff[stu.id][previousOff.id], " + ", previousOff.capacityCost

		# update attributes of new offering to reflect change
		stu.curOfferingID = newOff.id
		newOff.curSubscribed += 1
		if newOff.curSubscribed > newOff.maxCapacity:
			print "new offering is now oversubscribed"
			newOff.capacityCost += 1
			netConflict += 1
		newOff.pq.put((-stuXoff[stu.id][newOff.id], stu.id))

		# update attributes of previous offering to reflect change
		previousOff.curSubscribed -= 1
		if previousOff.capacityCost > 0:
			print "decrementing previous capacity cost"
			previousOff.capacityCost -= 1
			netConflict -= 1

		# update net conflict
		netConflict -= stuXoff[stu.id][previousOff.id]
		netConflict += stuXoff[stu.id][newOff.id]

		temperature *= rate

		if temperature < 0.01:
			temperature = 100.0
			print "TEMP RESET"

		iterations += 1

		print "New true cost: ", stuXoff[stu.id][newOff.id], " + ", newOff.capacityCost


		# DEBUG: 

		print "NET CONFLICT NOW == ", netConflict


	print "\n\nPROCESS FINISHED WITH NET CONFLICT: ", netConflict



def testValidity(studentList, offeringList):
	