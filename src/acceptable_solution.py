"""

Construct an acceptable matching of students to offerings (no age, grade, or capacity violations)
without taking any priority into account,
using minimum conflicts alg with simulated annealing

Receives lists of Student and Offering objects
Modifies student and offering properties to create pairs
DOES NOT add ghost students

"""

from random import randint
from util import *

def buildAcceptableSolution(studentList, offeringList, idToStudents, idToOfferings):
	
	netConflict = 0

	# students cross offerings: holds all static costs calculated for pairs
	stuXoff = [[None for i in range(len(offeringList))] for j in range(len(studentList))]


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
		offering.pq.put((cost, student.id))		# add student ID to offering's PQ

		netConflict += cost		# sum all static costs

	# now also add all capacity costs to netconflict
	for offering in offeringList:
		netConflict += offering.capacityCost


	print "INITIAL NET CONFLICT: ", netConflict

	print "STUXOFF: "
	for row in stuXoff:
		print row