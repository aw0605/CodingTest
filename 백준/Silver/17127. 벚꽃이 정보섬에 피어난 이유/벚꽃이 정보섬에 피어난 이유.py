import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans = 0
res1 = 1
for i in range(n-3):
    res1 *= arr[i]
    res2 = 1
    for j in range(i+1, n-2):
        res2 *= arr[j]
        res3 = 1
        for k in range(j+1, n-1):
            res3 *= arr[k]
            res4 = 1
            for l in range(k+1, n):
                res4 *= arr[l]
            ans = max(ans, res1 + res2 + res3 + res4)
            
print(ans)