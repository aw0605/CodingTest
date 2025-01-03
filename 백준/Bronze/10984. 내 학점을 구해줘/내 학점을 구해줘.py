import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    C = G = 0
    for _ in range(n):
        c,g = map(float, input().split())
        C += c
        G += c * g
    print(f"0 0.0" if not C else f"{int(C)} {G/C:.1f}")