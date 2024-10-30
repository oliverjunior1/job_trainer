from numpy.ma.extras import average

my_student = {
    'name':'Ralf Smith',
    'grades':[70,88,90,99]
}

def average_grade(student):
    return sum(student['grades'])/len(student['grades'])

print(average_grade(my_student))

class Student:
    def __init__(self, new_name, new_grade):
        self.name = new_name
        self.grade = new_grade

    def average(self):
        return sum(self.grade)/len(self.grade)

    def __str__(self):
        return f'The name of the student is {self.name}, the grade is: {self.average()}'

student_one = Student("Ralf Smith", [70,88,90,99])
student_two = Student("John Claud", [70,90,55,96])

# print(student_one.name)
# print(student_one.average())
#
# print(student_two.average())
print(student_one)
print(student_two)