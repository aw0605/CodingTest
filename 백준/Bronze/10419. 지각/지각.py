import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    d = int(input())
    ans = 0
    for i in range(1, d + 1):
        if i + (i ** 2) <= d: ans = i
        else: break
    print(ans)