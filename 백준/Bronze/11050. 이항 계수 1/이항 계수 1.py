import sys
input = sys.stdin.readline

n,k = map(int, input().split())

def facto(n):
  if n == 0 or n == 1: return 1
  else: return n * facto(n-1)

print(facto(n) // (facto(k) *facto(n-k)))