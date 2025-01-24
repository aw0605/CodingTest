import sys
input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]

for i,s in enumerate(arr):
    for j in range(i,n):
        if s[::-1] == arr[j]:
            l = len(s)
            print(l, s[l//2])
            break