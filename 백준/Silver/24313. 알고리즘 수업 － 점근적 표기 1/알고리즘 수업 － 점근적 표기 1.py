import sys
input = sys.stdin.readline

a,b = map(int, input().split())
c = int(input())
n0 = int(input())

def f(n):
    return a*n + b

correct = True
for n in range(n0, 101):
    if f(n) > c*n:
        correct = False
        break

print(1 if correct else 0)