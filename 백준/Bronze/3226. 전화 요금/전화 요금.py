import sys
input = sys.stdin.readline

n = int(input())
ans = 0
for _ in range(n):
    time,t = input().strip().split()
    h,m = map(int, time.split(":"))
    cur = h * 60 + m
    for i in range(int(t)):
        if 420 <= cur < 1140: ans += 10
        else: ans += 5
        cur += 1
        if cur == 1440: cur = 0
            
print(ans)