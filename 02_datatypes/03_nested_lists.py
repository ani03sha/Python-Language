# Given the names and grades for each student in a Physics class of N students, store them in a nested list and print
# the name(s) of any student(s) having the second lowest grade.
#
# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a
# new line.
if __name__ == '__main__':

    # List that will become the nested list eventually
    student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        # Adding names and scores in the list
        student.append([score, name])

    # Sort the list by score
    student.sort()

    # List comprehension
    b = [i for i in student if i[0] != student[0][0]]
    c = [j for j in b if j[0] == b[0][0]]

    # Sorting by name
    c.sort(key=lambda x: x[1])
    for i in range(len(c)):
        print(c[i][1])
