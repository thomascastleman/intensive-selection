
""" GLOBAL VARS: -------------------------------------- """

# number of offerings each student ranks
RANKSIZE = 5

# Priority coefficients
RPCOEFF = 0.2	# rank priority
GPCOEFF = 1.0	# grade priority
APCOEFF = 0.0	# age priority


""" --------------------------------------------------- """

import time

def main():
	
	import data.NonUniformTestData as td
	import solutions.initialCSP as csp
	import solutions.two_opt as tpt
	import evaluation as ev
	import util

	# construct all objects, and hashmaps
	students, offerings, idToStudents, idToOfferings = td.generateTestData(400, 20)

	# build solution
	print "Building initial randomized matching... ",
	start = time.time()
	csp.backTrackingSolution(0, students, offerings)
	print "Complete in {:.3f} seconds".format(time.time() - start)
	# csp.buildAcceptableSolution(students, offerings, idToStudents, idToOfferings)

	# run two-opt
	print "Beginning 2-opt optimization... \n",
	print "\nRP={:.3f}, GP={:.3f}, AP={:.3f}".format(RPCOEFF, GPCOEFF, APCOEFF)
	start = time.time()
	tpt.two_opt(students, offerings, idToOfferings)
	students = tpt.removeAllGhostStudents(students, idToOfferings)
	print "\nComplete in {:.3f} seconds".format(time.time() - start)

	# evaluate final solution
	print "\nRunning Evaluation..."
	ev.evaluate(students, offerings, idToStudents, idToOfferings, True)


if __name__ == "__main__":
	main()