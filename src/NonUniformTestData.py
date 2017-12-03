
"""
Students:
- even distribution across grades
- age should correlate with grade, but with some deviation
- intensive choice should not be uniform distribution

Offerings:
- max capacities should mostly be around (num students / num offerings)
- offering has either min grade or min age, or neither, but not both
	- only a small percentage of intensives should have these restrictions

"""

from classes.Student import Student
from classes.Offering import Offering
from main import rankSize, idToStudents, idToOfferings

from random import randint, uniform

import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.cm as cm
import numpy as np

# generate reasonable Student and Offering objects to test implementations
# returns tuple of ([student objects], [offering objects])
def generateTestData(numStudents, numOfferings):

	allGrades = [9, 10, 11, 12]		# grade levels
	normalAges = [15, 16, 17, 18]	# normal age for each grade level
	students, offerings = [], []	# arrays to hold objects
	
	# the way I'm doing it these are probably too uniform
	popularities = getPopularities(numOfferings)	# 0-1 that sum to 1

	# create as many students as requested
	for stuID in range(numStudents):
		# choose random grade
		grade = allGrades[randint(0, len(allGrades) - 1)]

		# age correlates, plus or minus 1
		age = normalAges[allGrades.index(grade)] + np.random.choice([-1, 0, 1], 1, p=[0.25, 0.5, 0.25])[0]

		# generate non-uniformly distributed rank
		rank = np.random.choice(numOfferings, rankSize, replace=False, p=popularities)

		s = Student(stuID, age, grade, rank)	# construct student
		idToStudents[stuID] = s					# add to global ID hashmap
		students.append(s)						# add to students array

	# create as many offerings as requested
	for offID in range(numOfferings):
		maxCap = int(numStudents / numOfferings) + randint(-5, 5)	# this is up for debate
		minGrade, minAge = 9, 0		# init at defaults
		if uniform(0, 1) < 0.2:
			# apply grade restriction
			if uniform(0, 1) < 0.5:
				# 11th grade likely to be min grade
				minGrade = np.random.choice(allGrades, 1, p=[0.0625, 0.1875, 0.6, 0.15])[0]
			# apply age restriction
			else:
				# higher ages more likely to be min age, if any restrictions imposed
				minAge = np.random.choice(normalAges, 1, p=[0.0625, 0.1875, 0.25, 0.5])[0]

		off = Offering(offID, maxCap, minGrade, minAge)		# construct offering
		idToOfferings[offID] = off							# add to global ID hashmap
		offerings.append(off)								# add to offerings array


	return students, offerings


	# ------------------------------------------------------

	# studentData = []
	# popularity = [0.21, 0.2, 0.11, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.04, 0.02,]

	# for student in range(308):
	#  studentData.append(np.random.choice(12, 5, replace=False, p=popularity))


	# totals = [0 for i in range(12)]
	# for student in range(308):
	# 	for rank in studentData[student]:
	# 		totals[rank]+=1
	# 	print studentData[student]
	# print "totals: ", totals 


	# y_pos = np.arange(12)

	 
	# plt.bar(y_pos, totals, align='center', alpha=0.5)
	# plt.xticks(y_pos, y_pos)
	# plt.ylabel('Frequency')
	# plt.xlabel('Intensive Choice')

	# plt.title('Choice Frequency')
	 
	# plt.show()


def getPopularities(n):
    nums = [uniform(0, 1) for i in range(n)]
    sum_ = 0
    for num in nums:
            sum_ += num
    for i in range(n):
            nums[i] /= sum_

    return nums