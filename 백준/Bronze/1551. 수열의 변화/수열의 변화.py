import sys
input = sys.stdin.readline

n,k = map(int, input().split())
a = list(map(int, input().split(",")))

for _ in range(k):
    b = [a[i+1] - a[i] for i in range(len(a)-1)]
    a = b
    
print(*a, sep=",")    