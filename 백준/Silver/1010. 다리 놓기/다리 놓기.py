import sys
input = sys.stdin.readline

def facto(n):
    num = 1
    for i in range(1, n+1): num *= i
    return num

t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    print(facto(m) // (facto(m-n) * facto(n)))