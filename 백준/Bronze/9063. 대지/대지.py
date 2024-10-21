import sys
input = sys.stdin.readline

n = int(input())
xArr = []
yArr = []

for _ in range(n):
    x,y = map(int, input().split())
    xArr.append(x)
    yArr.append(y)
    
w = max(xArr) - min(xArr)
h = max(yArr) - min(yArr)

print(w*h)
    