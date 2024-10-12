import sys

n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().strip()
    print(f"{s[0]}{s[-1]}")