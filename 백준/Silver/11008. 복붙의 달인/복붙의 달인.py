import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s,p = input().strip().split()
    ans = 0
    ans += s.count(p)
    rest = s.replace(p, "")
    ans += len(rest)
    print(ans)