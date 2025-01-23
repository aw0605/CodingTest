import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

h = 0
res = []
for i in range(n-1):
    if arr[i] < arr[i+1]: h += arr[i+1] - arr[i]
    else:
        res.append(h)
        h = 0
        
res.append(h)
print(max(res))