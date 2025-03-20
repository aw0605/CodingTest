import sys
input = sys.stdin.readline

s = 0
while True:
    n = int(input())
    if n == 0: break
    s += 1
    arr = [input().strip() for _ in range(n)]
    res = []
    for _ in range(2*n - 1):
        i,j = input().strip().split()
        res.append(int(i))
    idx = 0
    for i in range(1, n+1):
        if res.count(i) == 1:
            idx = i-1
            break
    print(s, arr[idx])