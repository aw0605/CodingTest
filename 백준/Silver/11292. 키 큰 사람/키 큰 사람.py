import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0: break
    students = {}
    maxH = 0
    for _ in range(n):
        a,b = input().strip().split()
        students[a] = float(b)
    for a,b in students.items():
        if b == max(students.values()): print(a, end=" ")
    print(end="\n")