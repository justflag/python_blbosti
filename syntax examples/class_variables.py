#class variables = Shared among all instaces of a class
# Defined ouside the constructor
# Allows you to share data among all objects created from that class

class Student:

    class_year = 2023 #class variable
    num_students = 0

    def __init__ (self, name, age):
        self.name = name #instance variable
        self.age = age
        Student.num_students += 1


student1 = Student("John", 20)
student2 = Student("Adam", 22)
student3 = Student("Cain", 9999)
student4 = Student("Joseph", 24)

print(student1.name)
print(student1.age)
#print(student1.class_year)
print(Student.class_year)
print(student2.name)
print(student2.age)
#print(student2.class_year)
print(Student.class_year) #preferred, access class varbile via class name
print(Student.num_students)
print(f"My graduating class of {Student.class_year} has {Student.num_students} students.")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)