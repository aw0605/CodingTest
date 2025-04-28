import sys
input = sys.stdin.readline

r, c = map(int, input().split())
arr = [input().strip() for _ in range(r)]

grade = 1
grades = [0] * 10
for i in range(c-2, 0, -1):
    flag = False
    for j in range(r):
        if arr[j][i] != "." and grades[int(arr[j][i])] == 0:
            grades[int(arr[j][i])] = grade
            flag = True
    if flag: grade += 1

for v in grades:
    if v: print(v)