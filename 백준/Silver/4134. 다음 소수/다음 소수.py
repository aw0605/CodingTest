import sys
import math
input = sys.stdin.readline

t = int(input())

def isPrime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0: return False
    return True

for i in range(t):
    n = (int(input()))
    while True:
        if isPrime(n):
            print(n)
            break
        else:
            n += 1