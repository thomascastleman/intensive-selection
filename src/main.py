
""" GLOBAL VARS: -------------------------------------- """

# number of offerings each student ranks
rankSize = 5

# Priority coefficients
rpCoeff = 1.0	# rank priority
gpCoeff = 1.0	# grade priority
apCoeff = 1.0	# age priority


""" --------------------------------------------------- """

import NonUniformTestData as td
import acceptable_solution as csp

def main():

	# construct all objects, and hashmaps
	students, offerings, idToStudents, idToOfferings = td.generateTestData(100, 5)

	# print "\n\nSTUDENTS: "
	# for stu in students:
	# 	stu.log()
	# print "\n\nOFFERINGS: "
	# for off in offerings:
	# 	off.log()

	csp.buildAcceptableSolution(students, offerings, idToStudents, idToOfferings)
	




if __name__ == "__main__":
	main()