import sys
input = sys.stdin.readline

def eratos(n,m):
    isPrime = [True] * (m+1)
    isPrime[0] = isPrime[1] = False
    for i in range(2, int(m**0.5)+1):
        if isPrime[i]:
            for j in range(i*i, m+1, i):
                isPrime[j] = False
    arr = [i for i in range(n,m+1) if isPrime[i]]
    return arr

n,m = map(int, input().split())

arr = eratos(n,m)

for num in arr:
    print(num)