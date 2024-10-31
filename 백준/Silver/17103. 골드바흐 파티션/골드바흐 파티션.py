import sys
input = sys.stdin.readline

t = int(input())

arr = [False]*2 + [True]*999999

for i in range(2, int(1000000**0.5)+1):
    if arr[i]:
        for j in range(i*i, 1000001, i):
            arr[j] = False

for _ in range(t):
    ans = 0
    n = int(input())
    for i in range(2, n//2+1):
        if arr[i] and arr[n-i]:
            ans += 1
    print(ans)
    