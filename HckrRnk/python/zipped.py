The National University conducts an examination of students in subjects.
Your task is to compute the average scores of each student.


n, x = map(inn, x = map(int, input().split(' '))

li = []
for _ in range(x):
    li += [list(map(float, input().split(' ')))]


lz = list(zip(*li))
for i in range(n):
    print(sum(list(lz[i]))/float(x))t, input().split(' '))

li = []
for _ in range(x):
    li += [list(map(float, input().split(' ')))]


lz = list(zip(*li))
for i in range(n):
    print(sum(list(lz[i]))/float(x))