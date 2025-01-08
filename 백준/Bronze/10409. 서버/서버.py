import sys
input = sys.stdin.readline

n,t = map(int, input().split())
times = list(map(int, input().split()))

ans = cur = 0
for time in times:
    if cur + time <= t:
        cur += time
        ans += 1
    else: break
        
print(ans)