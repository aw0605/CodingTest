import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0: break
    maxL = max(a,b,c)
    if maxL >= sum([a,b,c]) - maxL: print("Invalid")
    elif a == b == c: print("Equilateral")
    elif a != b and b != c and a != c: print("Scalene")
    else: print("Isosceles")

    