import sys
input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]
k = int(input())

if k == 2:
    for i in range(n): arr[i] = arr[i][::-1]
elif k == 3: 
    arr = arr[::-1]

for i in range(n):
    print(arr[i])