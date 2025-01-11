import sys
input = sys.stdin.readline

a,b,c = sorted(list(map(int, input().split())))
d1, d2 = b-a, c-b
if d1 == d2:  print(c + d1)
else:
    d = min(d1,d2)
    if d != d2: print(c - d)
    else: print(b - d)