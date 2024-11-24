import sys
input = sys.stdin.readline

t = int(input())

def sol():
    k = int(input())
    arr = list(map(int, input().split()))
    sub = [0] * (k + 1)
    
    rst = [[0] * k for _ in range(k)]
    opt = [[0] * k for _ in range(k)]
    
    for i in range(k): sub[i+1] = sub[i] + arr[i]
    for i in range(k): opt[i][i] = i

    for length in range(2, k + 1):
        for i in range(k - length + 1):
            j = i + length - 1
            rst[i][j] = float('inf')
            for l in range(opt[i][j-1], min(opt[i+1][j]+1, j)):
                cost = rst[i][l] + rst[l+1][j] + sub[j+1] - sub[i]
                if cost < rst[i][j]:
                    rst[i][j] = cost
                    opt[i][j] = l

    print(rst[0][k-1])

for _ in range(t): sol()