import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

m = max(arr)
scores = [(s / m) * 100 for s in arr]
    
print(sum(scores)/n)
    