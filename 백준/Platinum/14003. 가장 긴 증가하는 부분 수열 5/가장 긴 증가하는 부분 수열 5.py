import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

lis = [arr[0]]
dp = [(0,arr[0])] 

def bs(v):
    s,e = 0, len(lis) - 1 
    while s <= e:
        mid = (s + e) // 2
        if lis[mid] == v: return mid
        elif lis[mid] < v: s = mid + 1
        else: e = mid - 1
    return s

for i in range(1,n):
    if arr[i] > lis[-1]:
        lis.append(arr[i])
        dp.append((len(lis)-1, arr[i]))
    else:
        idx = bs(arr[i])
        lis[idx] = arr[i]
        dp.append((idx, arr[i]))

last = len(lis) - 1
res = []
for i in range(len(dp)-1, -1, -1):
    if dp[i][0] == last:
        res.append(dp[i][1])
        last -= 1
        
print(len(lis))
print(*res[::-1])