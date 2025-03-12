import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))

if n == 0:
    print(0)
    exit()

ans, w = 1, 0
for v in arr:
    if w + v <= m:
        w += v
    else:
        w = v
        ans += 1
        
print(ans)