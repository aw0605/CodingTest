import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    f = n % h
    if not f: f = h
    r = ((n - 1) // h) + 1
    print(f"{f}{r:02d}")