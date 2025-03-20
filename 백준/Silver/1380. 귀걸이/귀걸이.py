import sys
input = sys.stdin.readline

s = 0
while True:
    n = int(input())
    if n == 0: break
    s += 1
    arr = [input().strip() for _ in range(n)]
    res = set()
    for _ in range(2*n - 1):
        i,j = input().strip().split()
        num = int(i)
        if num in res: res.remove(num)
        else: res.add(num)
    print(s, arr[list(res)[0] - 1])