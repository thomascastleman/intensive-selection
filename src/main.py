
""" GLOBAL VARS: -------------------------------------- """

# number of offerings each student ranks
rankSize = 5

# Priority coefficients
rpCoeff = 1.0	# rank priority
gpCoeff = 1.0	# grade priority
apCoeff = 1.0	# age priority

# hashmaps of IDs to objects:
idToOfferings = {}
idToStudents = {}


""" --------------------------------------------------- """

from NonUniformTestData import generateTestData

def main():

	students, offerings = generateTestData(40, 10)

	print "\n\nSTUDENTS: "
	for stu in students:
		stu.log()
	print "\n\nOFFERINGS: "
	for off in offerings:
		off.log()


	
if __name__ == "__main__":
	main()