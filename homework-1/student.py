# TASK 2
#
# Write a base class to represent a student. Below is a starter code.
# Feel free to add any more new features to your class.
# As a minimum a student has a name and age and a unique ID.
#
# Create a new subclass from student to represent a concrete student doing a specialization, for example:
# Software Student and Data Science student.

"""


class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()


# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)

"""
from statistics import mean

class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

    def student_name(self):
        return print(f"The students full name is {self.name}")


    def student_information(self):
        return print(f"ID number {self.id}, Details: {self.name}, {self.age} years old")


class CFGStudent(Student):

    def __init__(self, name, age, id, specialization, subjects=None):
        super().__init__(name, age, id)
        self.specialization = specialization
        self.subjects = subjects or dict()


    def add_subject(self, subjects, grade):
        self.subjects.update({subjects: grade})
        return subjects


    def remove_subject(self,subjects):
        self.subjects.pop(subjects)
        return subjects


    def total_subjects(self):
        return print(self.subjects)

    def average_grade(self):
        average_mark = (sum(self.subjects.values())/len(self.subjects))
        return print(f"The average mark for {self.name} is {average_mark}")


#Class of students
student_1 = CFGStudent(name="Harry", age=10, id=1001, specialization="wizard")
student_2 = CFGStudent(name="Ron", age=11, id=1002, specialization="wizard")
student_3 = CFGStudent(name="Hermoine", age=9, id=1003, specialization="witch", subjects={"pottery": 10})
student_4 = CFGStudent(name="Hagrid", age=22, id=1004, specialization="grounder")

#student_1
student_1.student_name()
student_1.student_information()
student_1.add_subject("potions", 5)
student_1.add_subject("games", 10)
student_1.add_subject("gardening", 4)
student_1.remove_subject("gardening")
student_1.total_subjects()
student_1.average_grade()

#student_2
student_2.student_name()
student_2.student_information()
student_2.add_subject("potions", 9)
student_2.add_subject("games", 2)
student_2.add_subject("gardening", 10)
student_2.remove_subject("potions")
student_2.total_subjects()
student_2.average_grade()

#student_2
student_3.student_name()
student_3.student_information()
student_3.add_subject("dance", 5)
student_3.add_subject("potions", 10)
student_3.remove_subject("potions")
student_3.total_subjects()
student_3.average_grade()

#student_4
student_4.student_name()
student_4.student_information()
student_4.add_subject("dance", 2)
student_4.add_subject("forestry", 10)
student_4.add_subject("gardening", 10)
student_4.total_subjects()
student_4.average_grade()


