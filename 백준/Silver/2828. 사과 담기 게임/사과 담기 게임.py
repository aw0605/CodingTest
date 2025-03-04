import sys
input = sys.stdin.readline

n,m = map(int, input().split())
j = int(input())
arr = [int(input()) for _ in range(j)]

cur, ans = 1, 0
for v in arr:
    if cur <= v and cur + (m-1) >= v: continue
    elif cur > v:
        ans += abs(v - cur)
        cur = v
    else: 
        ans += v - (m-1) - cur
        cur = v - (m-1)
        
print(ans)