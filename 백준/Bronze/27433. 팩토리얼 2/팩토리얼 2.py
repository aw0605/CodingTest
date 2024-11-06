import sys

n = int(sys.stdin.readline())

def facto(n):
    if n <= 1: return 1
    else: return n * facto(n-1)

print(facto(n))