import sys

h,m = map(int, sys.stdin.readline().split())
time = int(sys.stdin.readline())

m += time

while m > 59:
    m -= 60
    h += 1
    if h > 23: h -= 24

print(h,m)