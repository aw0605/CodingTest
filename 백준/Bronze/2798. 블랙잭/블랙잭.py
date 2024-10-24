import sys
from itertools import combinations

input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))

comb = list(combinations(arr,3))

ans = 0

for v in comb:
    cur = sum(v)
    if cur == m:
        ans = cur
        break
    elif cur > ans and cur <= m: ans = cur
        
print(ans)
