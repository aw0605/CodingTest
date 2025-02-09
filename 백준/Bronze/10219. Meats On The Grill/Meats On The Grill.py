import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h,w = map(int, input().split())
    grill = [input().strip() for _ in range(h)]
    for row in grill: print(row[::-1])