import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input().strip() for _ in range(n)]

r = sum(1 for row in arr if "X" not in row)
c = sum(1 for col in zip(*arr) if "X" not in col)

print(max(r, c))