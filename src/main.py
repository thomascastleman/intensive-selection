
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

		off.log()

	print age, " offerings with age restrictions"
	print grade, " offerings with grade restrictions"
	print totalCap - len(students), " extra positions"

	# build solution
	csp.buildAcceptableSolution(students, offerings, idToStudents, idToOfferings)

	# print "\n\nSTUDENTS: "
	# for stu in students:
	# 	stu.log()
	# print "\n\nOFFERINGS: "
	# for off in offerings:
	# 	off.log()





if __name__ == "__main__":
	main()