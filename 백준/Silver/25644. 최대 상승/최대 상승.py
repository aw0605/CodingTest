import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

maxDiff = 0
minV = arr[0]
for i in range(1,n):
    if minV > arr[i]: minV = arr[i]
    else:
        res = arr[i] - minV
        if maxDiff < res: maxDiff = res
            
print(maxDiff)