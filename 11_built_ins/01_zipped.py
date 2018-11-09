# The National University conducts an examination of N students in X subjects.
# Your task is to compute the average scores of each student.


n, x = map(int, input().split())
scores = []
for _ in range(x):
    scores.append(map(float, input().split()))
for i in zip(*scores):
    print(sum(i) / len(i))
