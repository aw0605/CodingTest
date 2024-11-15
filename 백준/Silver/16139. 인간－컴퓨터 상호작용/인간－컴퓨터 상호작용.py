import sys
input = sys.stdin.readline

s = input().strip()
n = int(input())

for _ in range(n):
    alpha, l, r = input().strip().split()
    print(s[int(l):int(r)+1].count(alpha))