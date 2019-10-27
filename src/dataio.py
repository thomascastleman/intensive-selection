
import os
from datetime import datetime

MATCHING_OUTPUT_FILE = os.getcwd() + "/output/matching.csv"

""" Reads data files and constructs two lists: one of Student objects, one of Offering objects, 
    as well as two hashmaps: Student ID to Student object, and Offering ID to Offering object
    The return value is a 4-tuple: (students, offerings, idToStudent, idToOffering) """
def constructObjects():
  pass

# given a list of objects with IDs, construct a mapping from IDs to objects
def mapIDtoObject(lst):
  hashmap = {}
  for obj in lst:
    hashmap[obj.id] = obj
  return hashmap

# Serializes a matching into human-readable CSV form
def writeMatchingToFile(students, offerings, idToStudents, idToOfferings):
  for stu in students:
    off = idToOfferings[stu.curOfferingID]

    if off is not None:
      # add Student object to Offering's roster
      off.subscribedStudents.append(stu)

  f = open(MATCHING_OUTPUT_FILE, "w+")

  # record timestamp of writing matching
  timestamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S") # mm/dd/YY H:M:S
  f.write("Generated on " + timestamp + "\n\n")

  # sort offerings by ID before writing
  offerings = sorted(offerings, key=lambda off: off.id)

  for off in offerings:
    f.write("----------------------------------------------------------------------------------------------------------------------------------------\n")

    # add header for intensive metadata
    f.write("Intensive Name,ID,Min. Age,Min. Grade,Max. Cap.\n")

    # use N/A values instead of representational defaults if no min age or grade
    minAge = off.minAge if off.minAge != 0 else "N/A"
    minGrade = off.minGrade if off.minGrade != 9 else "N/A"

    fields = map(lambda f: "\"" + str(f) + "\"", [off.name, off.id, minAge, minGrade, off.maxCapacity])
    f.write(",".join(fields) + "\n\n")

    # add header for student metadata
    f.write("Assigned Student,Email,Age,Grade,Prefs\n")

    # for each student assigned to this intensive
    for stu in off.subscribedStudents:
      prefs = "N/A" if stu.rank == [] else stu.rank
      fields = map(lambda f: "\"" + str(f) + "\"", [stu.name, stu.email, stu.age, stu.grade, stu.rank])
      f.write(",".join(fields) + "\n")

  
  f.write("----------------------------------------------------------------------------------------------------------------------------------------\n")
  f.close()