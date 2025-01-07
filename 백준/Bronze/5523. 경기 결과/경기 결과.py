import sys
input = sys.stdin.readline

n = int(input())

res = [0,0]
for _ in range(n):
    a,b = map(int, input().split())
    if a > b: res[0] += 1
    elif a < b: res[1] += 1
        
print(" ".join(map(str, res)))