from math import ceil
import sys
input = sys.stdin.readline

n = int(input())
tee = list(map(int, input().split()))
t,p = map(int, input().split())

tAns = 0
for v in tee:
    tAns += ceil(v / t)
    
print(tAns)
print(n // p, n % p)