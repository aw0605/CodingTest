import sys
input = sys.stdin.readline

a,b = map(int, input().split())
m = int(input())
arr = list(map(int, input().split()))[::-1]

x = 0
res = []
for i in range(m): x += arr[i] * (a**i)
    
while x != 0:
    res.append(x % b)
    x //= b
    
print(" ".join(map(str, res[::-1])))