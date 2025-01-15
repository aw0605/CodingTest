import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    for _ in range(n):
        li = list(map(int, input().split()))
        m = max(li)
        if m <= 0: continue
        else: ans += m
    print(ans)