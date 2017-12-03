
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

import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.cm as cm
import numpy as np

# generate reasonable Student and Offering objects to test implementations
# returns tuple of ([student objects], [offering objects])
def generateTestData(numStudents, numOfferings):

	


	# --------------------------------------

	studentData = []
	popularity = [0.21, 0.2, 0.11, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.04, 0.02,]

	for student in range(308):
	 studentData.append(np.random.choice(12, 5, replace=False, p=popularity))


	totals = [0 for i in range(12)]
	for student in range(308):
		for rank in studentData[student]:
			totals[rank]+=1
		print studentData[student]
	print "totals: ", totals 


	y_pos = np.arange(12)

	 
	plt.bar(y_pos, totals, align='center', alpha=0.5)
	plt.xticks(y_pos, y_pos)
	plt.ylabel('Frequency')
	plt.xlabel('Intensive Choice')

	plt.title('Choice Frequency')
	 
	plt.show()