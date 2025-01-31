import sys
input = sys.stdin.readline

yj = list(map(int, input().split()))
sg = list(map(int, input().split()))

s1 = s2 = 0
reverse = 0
for a, b in zip(yj, sg):
    s1 += a
    if s1 > s2: reverse = 1
    s2 += b

print("Yes" if reverse and s1 < s2 else "No")