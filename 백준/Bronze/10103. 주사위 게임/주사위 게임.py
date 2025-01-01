import sys
input = sys.stdin.readline

n = int(input())

c,s = 100,100
for _ in range(n):
    a,b = map(int, input().split())
    if a == b: continue
    elif a > b: s -= a
    else: c -= b
        
print(c)
print(s)