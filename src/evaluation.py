"""
Used to evaluate the solutions generated by different algs

Give stats like:
	- percentage of students with each choice (first, second ...)
	- percentage of students paired with none of their choices

	- for each grade, percentage of students with first choice

	- percentage full for each intensive (num students assigned / max capacity)

"""

from main import rankSize, idToOfferings, idToStudents

def evaluate(studentList, offeringList):
	
	choices = [0 for i in range(rankSize + 1)]

	for student in studentList:

		offering = idToOfferings[student.curOfferingID]

		if offering.id not in student.rank:
			index = rankSize
		else:
			index = student.rank.index(offering.id)

		choices[index] += 1

	# percentage for each choice: choices[index] / number of students
