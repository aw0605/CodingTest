import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == 0: break
    arr = sorted([a, b, c])
    if arr[2] >= arr[0] + arr[1]: print("Invalid")
    elif a == b == c: print("Equilateral")
    elif a == b or b == c or c == a: print("Isosceles")
    else: print("Scalene")

    