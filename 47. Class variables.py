# Class Variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share among all objects created from that class

class Student:

    class_year = 2020
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Rio", 30)
student2 = Student("Lil", 25)
student3 = Student("Marianna", 30)
student4 = Student("Julia", 20)

# print(student1.name)
# print(student2.age)
# print(student2.class_year)
#
# print(student2.name)
# print(student2.age)
# print(student2.class_year)
#
# print(Student.class_year)

# print(Student.num_students)

print(f"My graduating class of {Student.class_year}, has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)