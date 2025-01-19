import sys
input = sys.stdin.readline

n,k,p = map(int, input().split())
breads = list(map(int, input().split()))

ans = 0
for i in range(0,n*k,k):
    if breads[i:i+k].count(0) < p: ans += 1

print(ans)