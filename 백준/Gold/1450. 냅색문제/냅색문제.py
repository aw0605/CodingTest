from itertools import combinations
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
weights = list(map(int, input().split()))

w1, w2 = weights[:n//2], weights[n//2:]
sum1, sum2 = [],[]

for i in range(len(w1) + 1):
    comb1 = combinations(w1, i)
    for comb in comb1:
        sum1.append(sum(comb))
        
for i in range(len(w2) + 1):
    comb2 = combinations(w2, i)
    for comb in comb2:
        sum2.append(sum(comb))

sum1.sort()

ans = 0

for v in sum2:
    if v > c: continue
    l,r = 0, len(sum1) - 1
    while l <= r:
        mid = (l + r) // 2
        if sum1[mid] + v > c: r = mid - 1    
        else: l = mid + 1
    ans += r + 1

print(ans)