import sys
input = sys.stdin.readline

n,m = map(int, input().split())

limits = []
real = []
for _ in range(n):
    l,s = map(int, input().split())
    for i in range(l): limits.append(s)
for _ in range(m):
    l,s = map(int, input().split())
    for i in range(l): real.append(s)
        
ans = 0
for i in range(100):
    ans = max(ans, real[i] - limits[i])
        
print(ans)