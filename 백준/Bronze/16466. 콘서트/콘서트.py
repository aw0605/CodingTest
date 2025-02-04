import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
for i in range(1,n+1):
    if arr[i-1] != i:
        print(i)
        exit()
print(n+1)