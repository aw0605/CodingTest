import sys
input = sys.stdin.readline

n,k = map(int, input().split())
p = 1000000007

def facto(n):
    num = 1
    for i in range(2,n+1): num = (num * i) % p
    return num

def square(n,k):
    if k == 0: return 1
    elif k == 1: return n
    tmp = square(n,k//2)
    if k % 2 == 0: return (tmp * tmp) % p
    else: return (tmp * tmp * n) % p

numer = facto(n)
denom = facto(k) * facto(n-k) % p

print(numer * square(denom, p-2) % p)