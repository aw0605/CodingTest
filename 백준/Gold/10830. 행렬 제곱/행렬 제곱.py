import sys
input = sys.stdin.readline

n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def multi(a, b):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += (a[i][k] * b[k][j])
                res[i][j] %= 1000
    return res

def square(arr, b):
    if b == 1: return [[n % 1000 for n in row] for row in arr]
    tmp = square(arr, b // 2)
    if b % 2 == 0: return multi(tmp, tmp)
    else: return multi(multi(tmp, tmp), arr)

ans = square(arr, b)

for row in ans:
    print(*row)