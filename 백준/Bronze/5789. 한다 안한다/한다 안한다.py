import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().strip()
    while len(s) > 2: s = s[1:-1]
    if s[0] == s[1]: print("Do-it")
    else: print("Do-it-Not")