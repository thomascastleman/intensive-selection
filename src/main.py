
""" GLOBAL VARS: -------------------------------------- """

# number of offerings each student ranks
RANKSIZE = 5

# Priority coefficients
RPCOEFF = 1.0	# rank priority
GPCOEFF = 0.75	# grade priority
APCOEFF = 0.0	# age priority


""" --------------------------------------------------- """

import NonUniformTestData as td
import acceptable_solution as csp
import two_opt as tpt
import evaluation as ev
import util

def main():

	# construct all objects, and hashmaps
	students, offerings, idToStudents, idToOfferings = td.generateTestData(400, 20)

	# build solution
	csp.backTrackingSolution(0, students, offerings)

	# calculate age priorities before two-opt
	util.initAllAgeP(students)

	# run two-opt
	tpt.two_opt(students, offerings, idToOfferings)
	students = tpt.removeAllGhostStudents(students, idToOfferings)

	# evaluate final solution
	ev.evaluate(students, offerings, idToStudents, idToOfferings)


if __name__ == "__main__":
	main()