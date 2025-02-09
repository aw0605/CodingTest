import sys
input = sys.stdin.readline

n,m = map(int, input().split())
S = input().strip()

for _ in range(m):
    post = input().strip()
    i = 0
    for v in post:
        t = S[i]
        if v != t: continue
        i += 1
        if i >= n: break
    print("true" if n == i else "false")