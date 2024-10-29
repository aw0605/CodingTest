import sys
input = sys.stdin.readline

n,m = map(int, input().split())

S = set(input().strip() for _ in range(n))
M = [input().strip() for _ in range(m)]
ans = 0

for v in M:
    if v in S: ans += 1

print(ans)