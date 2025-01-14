import sys
input = sys.stdin.readline

n, m = map(int, input().split())

for i in range(1, n+1):
    print(" ".join(map(str, range((i - 1) * m + 1, i * m + 1))))