# UTILITIES / COST FUNCTIONS ETC.

from main import rpCoeff, gpCoeff, apCoeff

# calculate cost of a pair with respect to PRIORITIES (weighted with coefficients)
def softCost(pair):
	student, offering = pair
	if student.isGhost:
		return 0
	else:
		# rank priority: in range (0, 1), equal to position of offering on student's rank over num possible positions (rankSize + 1)
		rankP = 1 if offering.id not in student.rank else (student.rank.index(offering.id) + 1) / (rankSize + 1)

		return (rpCoeff * rankP) + (gpCoeff * student.gradeP) + (apCoeff * student.ageP)

# calculate cost of a pair with respect to the age / grade HARD CONSTRAINTS (does not factor in capacity cost)
def staticCost(pair):
	student, offering = pair
	return (1 if student.age < offering.minAge else 0) + (1 if student.grade < offering.minGrade else 0)

# determine if a pair is legal based on grade / age restrictions
def isLegal(pair):
	student, offering = pair
	return student.isGhost or (student.grade >= offering.minGrade and student.age >= offering.minAge)

# calculate age priority values for all students in a given set
def initAllAgeP(students):
	if apCoeff != 0.0:
		minAge = students[0].age
		maxAge = students[0].age

		for student in students:
			if student.age < minAge:
				minAge = student.age
			elif student.age > maxAge: 
				maxAge = student.age

		ageRange = maxAge - minAge

		for student in students:
			student.ageP = (maxAge - student.age + 1) / ageRange