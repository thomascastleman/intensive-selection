
""" GLOBAL VARS: -------------------------------------- """

# number of offerings each student ranks
rankSize = 5

# Priority coefficients
rpCoeff = 1.0	# rank priority
gpCoeff = 1.0	# grade priority
apCoeff = 0.0	# age priority


""" --------------------------------------------------- """

import NonUniformTestData as td
import acceptable_solution as csp
import two_opt as tpt
import evaluation as ev
from util import *

def main():

	# construct all objects, and hashmaps
	students, offerings, idToStudents, idToOfferings = td.generateTestData(400, 20)

	age = 0
	grade = 0
	totalCap = 0

	for off in offerings:
		if off.minGrade > 9:
			grade += 1
		if off.minAge > 0:
			age += 1

		totalCap += off.maxCapacity

	print age, " offerings with age restrictions"
	print grade, " offerings with grade restrictions"
	print totalCap - len(students), " extra positions"

	# build solution
	csp.buildAcceptableSolution(students, offerings, idToStudents, idToOfferings)

	# calculate age priorities before two-opt
	initAllAgeP(students)

	# run two-opt
	tpt.two_opt(students, offerings, idToOfferings)
	students = tpt.removeAllGhostStudents(students, idToOfferings)

	# evaluate final solution
	ev.evaluate(students, offerings, idToStudents, idToOfferings)


if __name__ == "__main__":
	main()