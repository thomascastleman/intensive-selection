
""" GLOBAL VARS: -------------------------------------- """

# number of offerings each student ranks
RANKSIZE = 5

# Priority coefficients
RPCOEFF = 1.0	# rank priority
GPCOEFF = 0.75	# grade priority
APCOEFF = 0.0	# age priority

# minimum acceptable percent first choice overall
percentThreshold = 0.0

""" --------------------------------------------------- """

import time	# for runtime

def main():

	import data.NonUniformTestData as td
	import evaluation as ev

	# construct all objects, and hashmaps
	students, offerings, idToStudents, idToOfferings = td.generateTestData(400, 20)

	# use 2-opt technique
	students = runTwoOpt(students, offerings, idToStudents, idToOfferings, True, percentThreshold)

	# evaluate final solution
	print "\nRunning Evaluation..."
	ev.evaluate(students, offerings, idToStudents, idToOfferings, False)



# run a full 2-opt solution on a set of student and offering objects
def runTwoOpt(students, offerings, idToStudents, idToOfferings, logging, threshold):

	import solutions.initialCSP as csp
	import solutions.two_opt as tpt
	import evaluation as ev

	print "\nMinimum Acceptable Percentage First Choice: {:.2f}%".format(threshold)

	while True:

		# build solution
		if logging: print "Building initial randomized matching... ",
		start = time.time()
		csp.backTrackingSolution(0, students, offerings)
		if logging: print "Complete in {:.3f} seconds".format(time.time() - start)
		# csp.buildAcceptableSolution(students, offerings, idToStudents, idToOfferings)

		# run two-opt
		if logging: 
			print "Beginning 2-opt optimization... \n",
			print "\nRP={:.3f}, GP={:.3f}, AP={:.3f}".format(RPCOEFF, GPCOEFF, APCOEFF)
		start = time.time()
		tpt.two_opt(students, offerings, idToOfferings, logging)
		students = tpt.removeAllGhostStudents(students, idToOfferings)
		if logging: print "\nComplete in {:.3f} seconds".format(time.time() - start)


		# evalulate and run again if necessary
		percent = ev.getPercentFirstChoice(students)
		print "Solution found with " + str(percent) + "%"

		if percent >= threshold:
			break
		else:
			# reset pairings
			for off in offerings:
				off.curSubscribed = 0

	return students

if __name__ == "__main__":
	main()