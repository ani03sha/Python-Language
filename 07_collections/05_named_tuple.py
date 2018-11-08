# Dr. John Wesley has a spreadsheet containing a list of student's IDs, class, marks and name.
#
# Your task is to help Dr. Wesley calculate the average marks of the students.
# Note:
# 1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
# 2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)


from collections import namedtuple

n, fields = int(input()), input().split()
sum = 0
for i in range(n):
    Students = namedtuple('Student', fields)
    field1, field2, field3, field4 = input().split()
    student = Students(field1, field2, field3, field4)
    sum += int(student.MARKS)
print('{:.2f}'.format(sum / n))
