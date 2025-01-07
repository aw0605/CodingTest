import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    S = input().strip()
    ans = 0
    for v in range(65, 91):
        if chr(v) not in S: ans += v
    print(ans)