import sys
input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]

for i,s in enumerate(arr):
    if s[::-1] in arr[i:]:
        l = len(s)
        print(l, s[l//2])
        break