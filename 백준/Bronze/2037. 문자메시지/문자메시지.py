import sys
input = sys.stdin.readline

keyboard = ["", " ", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

p, w = map(int, input().split())
S = input().strip()
ans = 0
prev = -1
for s in S:
    for n, text in enumerate(keyboard):
        if s in text:
            cnt = text.index(s) + 1
            ans += cnt * p
            if prev == n and n != 1: ans += w
            prev = n
            break

print(ans)