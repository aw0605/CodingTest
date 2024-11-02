import sys
input = sys.stdin.readline

n = int(input())

power = 1
while power * 2 <= n:
    power *= 2

print(n if n == power else 2*(n-power))