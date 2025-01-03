import sys
input = sys.stdin.readline

def isEven(n):
    if not n % 2: return True
    else: return False

t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    evens = [n for n in nums if isEven(n)]
    print(sum(evens), min(evens))