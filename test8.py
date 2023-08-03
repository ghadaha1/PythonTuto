class Student:
    def __int__(self, name, age=0, courses=""):
        self.name = name
        self.age = age
        self.courses = courses


student = Student("is",15)
print(student)
