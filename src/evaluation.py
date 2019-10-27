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
import os
from main import RANKSIZE
from datetime import datetime

EVAL_FILE_OUT = os.getcwd() + "/output/evaluation.csv"

def evaluate(studentList, offeringList, idToStudents, idToOfferings, showPlots):
  # open evaluation file for writing output logs
  f = open(EVAL_FILE_OUT, "w+")

  choices = [0 for i in range(RANKSIZE + 1)]  # number of students receiving each choice
  grades = [0 for i in range(4)]  # number of students receiving first choice in each of the four grades
  gradeCounts = [0 for i in range(4)] # total number of people in each grade

  # num students for each choice per grade
  choicePerGrade = [[0 for c in range(RANKSIZE + 1)] for g in range(4)]
  indexToString = {0 : "Freshmen", 1 : "Sophomores", 2 : "Juniors", 3 : "Seniors"}

  for student in studentList:
    
    offering = idToOfferings[student.curOfferingID] # get offering object

    # get position on student's rank
    if offering.id not in student.rank:
      index = RANKSIZE
    else:
      index = student.rank.index(offering.id)

    choices[index] += 1 # increment number of students with this choice
    gradeCounts[[9, 10, 11, 12].index(student.grade)] += 1  # increment num students in this grade

    # if first choice, increment record of first choice students in this grade
    if index == 0:
      grades[[9, 10, 11, 12].index(student.grade)] += 1

    # increment num students in this grade for this choice
    choicePerGrade[[9, 10, 11, 12].index(student.grade)][index] += 1



  # mark time eval report was generated
  timestamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S") # mm/dd/YY H:M:S
  log(f, "Generated on " + timestamp + "\n")

  # start logging eval
  log(f, "__________________________________________________________________")
  log(f, "\nEVALUATION OF MATCHING BETWEEN " + str(len(studentList)) + " STUDENTS AND " + str(len(offeringList)) + " OFFERINGS:\n")


  log(f, "Percentage of each choice out of all students")
  for i in range(len(choices)):
    if i == len(choices) - 1:
      percentage = float(choices[i]) / len(studentList) * 100.0
      log(f, "Arbitrary: \t{:.3f}%".format(percentage))
    else:
      percentage = float(choices[i]) / len(studentList) * 100.0
      log(f, "Choice " + str(i + 1) + ": \t{:.3f}%".format(percentage))

  log(f, "\nPercentage full for each intensive:")
  total = 0 # sum of all capacity percentages
  minPercent = None
  maxPercent = None

  minNumStudents = None
  maxNumStudents = None

  subscribed = []

  # sort offerings by ID before writing
  offeringList = sorted(offeringList, key=lambda off: off.id)

  log(f, "ID \tPercent of capacity filled")
  for offering in offeringList:
    subscribed.append(offering.curSubscribed)
    percentage = float(offering.curSubscribed) / offering.maxCapacity * 100.0
    log(f, str(offering.id) + ": \t{:.3f}% \t({} students) \t({} max)".format(percentage, offering.curSubscribed, offering.maxCapacity))

    total += percentage
    if minPercent == None or percentage < minPercent:
      minPercent = percentage
      minNumStudents = offering.curSubscribed
    if maxPercent == None or percentage > maxPercent:
      maxPercent = percentage
      maxNumStudents = offering.curSubscribed

  log(f, "\nAverage Percent Full: \t{:.3f}%".format(total / len(offeringList)))
  log(f, "Min Percent Full: \t{:.3f}% with {} students".format(minPercent, minNumStudents))
  log(f, "Max Percent Full: \t{:.3f}% with {} students".format(maxPercent, maxNumStudents))

  log(f, "\nGrade-wise stats: ")
  for g in range(len(choicePerGrade)):
    ch = choicePerGrade[g]
    gradeString = indexToString[g]
    stuInThisGrade = gradeCounts[g]

    log(f, "\n" + gradeString + ": ")
    for c in range(len(ch)):
      percentage = float(ch[c]) / stuInThisGrade * 100.0
      if c == len(ch) - 1:
        log(f, "Arbitrary: \t{:.3f}%".format(percentage))
      else:
        log(f, "Choice " + str(c + 1) + ": \t{:.3f}%".format(percentage))

  log(f, "\n__________________________________________________________________")

  # close evaluation output file
  f.close()

  # PLOTS:

  if showPlots:
    print "Showing Plots... "

    ch = [i for i in range(1, RANKSIZE + 2)]
    plt.bar(ch, choices, align='center', alpha=0.5)
    plt.xlabel('Choice (' + str(RANKSIZE + 1) + ' arb)')
    plt.ylabel('Students')
    plt.title('Students per choice')
    plt.show()

    off = [i + 1 for i in range(len(offeringList))]
    plt.bar(off, subscribed, align='center', alpha=0.5)
    plt.xticks(np.arange(1, len(offeringList) + 1))
    plt.xlabel('Offering')
    plt.ylabel('Students')
    plt.title('Student Distribution')
    plt.show()


def getPercentFirstChoice(students):

  numFirst = 0

  for stu in students:
    if stu.curOfferingID in stu.rank and stu.rank.index(stu.curOfferingID) == 0:
      numFirst += 1

  return float(numFirst) / len(students) * 100.0


# both print text to console and write it to the given file
def log(f, content):
  print content

  formatted = ",".join(content.split(" \t"))

  f.write(formatted + "\n")