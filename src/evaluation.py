"""
Used to evaluate the solutions generated by different algs

Give stats like:
	- percentage of students with each choice (first, second ...)
	- percentage of students paired with none of their choices

	- for each grade, percentage of students with first choice

	- percentage full for each intensive (num students assigned / max capacity)

"""

import numpy as np
import matplotlib.pyplot as plt

from main import rankSize

def evaluate(studentList, offeringList, idToStudents, idToOfferings):

	choices = [0 for i in range(rankSize + 1)]	# number of students receiving each choice
	grades = [0 for i in range(4)]	# number of students receiving first choice in each of the four grades
	gradeCounts = [0 for i in range(4)]	# total number of people in each grade

	for student in studentList:
		
		offering = idToOfferings[student.curOfferingID]	# get offering object

		# get position on student's rank
		if offering.id not in student.rank:
			index = rankSize
		else:
			index = student.rank.index(offering.id)

		choices[index] += 1	# increment number of students with this choice
		gradeCounts[[9, 10, 11, 12].index(student.grade)] += 1	# increment num students in this grade

		# if first choice, increment record of first choice students in this grade
		if index == 0:
			grades[[9, 10, 11, 12].index(student.grade)] += 1

	# Format results and print to console:
	print "\n-------------------------------------------------------------------"
	print "\nEVALUATION OF MATCHING BETWEEN " + str(len(studentList)) + " STUDENTS AND " + str(len(offeringList)) + " OFFERINGS:\n"


	print "Percentage of each choice out of all students"
	for i in range(len(choices)):
		if i == len(choices) - 1:
			percentage = float(choices[i]) / len(studentList) * 100.0
			print "Arbitrary:\t{:.3f}%".format(percentage)
		else:
			percentage = float(choices[i]) / len(studentList) * 100.0
			print "Choice " + str(i + 1) + ":\t{:.3f}%".format(percentage)

	print "\nPercentage first choice per grade"
	for i in range(len(grades)):
		percentage = float(grades[i]) / gradeCounts[i] * 100.0
		print "Grade " + str(i + 9) + ":\t{:.3f}%".format(percentage)

	print "\nPercentage full for each offering:\n"
	total = 0 # sum of all capacity percentages
	minPercent = None
	maxPercent = None

	subscribed = []

	print "ID\tPercent of capacity filled"
	for offering in offeringList:
		subscribed.append(offering.curSubscribed)
		percentage = float(offering.curSubscribed) / offering.maxCapacity * 100.0
		print str(offering.id) + ": \t{:.3f}%".format(percentage)

		total += percentage
		if minPercent == None or percentage < minPercent:
			minPercent = percentage
		if maxPercent == None or percentage > maxPercent:
			maxPercent = percentage

	print "\nAverage Percent Full: {:.3f}%".format(total / len(offeringList))
	print "Min Percent Full: {:.3f}%".format(minPercent)
	print "Max Percent Full: {:.3f}%".format(maxPercent)

	print "\n-------------------------------------------------------------------"

	ch = [i for i in range(1, rankSize + 2)]
	plt.bar(ch, choices, align='center', alpha=0.5)
	plt.xlabel('Choice (' + str(rankSize + 1) + ' arb)')
	plt.ylabel('Students')
	plt.title('Students per choice')
	plt.show()

	grd = [i + 9 for i in range(4)]
	plt.bar(grd, grades, align='center', alpha=0.5)
	plt.xticks(np.arange(9, 13))
	plt.xlabel('Grade')
	plt.ylabel('Students')
	plt.title('Students per grade with first choice')
	plt.show()

	off = [i + 1 for i in range(len(offeringList))]
	plt.bar(off, subscribed, align='center', alpha=0.5)
	plt.xticks(np.arange(1, len(offeringList) + 1))
	plt.xlabel('Offering')
	plt.ylabel('Students')
	plt.title('Student Distribution')
	plt.show()