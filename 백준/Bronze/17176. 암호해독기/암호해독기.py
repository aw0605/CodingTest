import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = sorted(input().strip())

AB = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ab = "abcdefghijklmnopqrstuvwxyz"

res = []
for s in arr:
    if s == 0: res.append(" ")
    elif 1 <= s <= 26: res.append(AB[s-1])
    elif 27 <= s <= 52: res.append(ab[s-27])

print("y" if ans == sorted(res) else "n")