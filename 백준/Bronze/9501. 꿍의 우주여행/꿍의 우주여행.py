import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,d = map(int, input().split())
    ans = 0
    for _ in range(n):
        v,f,c = map(int, input().split())
        if (d / v) * c <= f: ans += 1
    print(ans)