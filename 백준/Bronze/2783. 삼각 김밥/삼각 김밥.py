import sys
input = sys.stdin.readline

perPrices = []
sx, sy = map(int, input().split())
perPrices.append(sx/sy)
n = int(input())
for _ in range(n):
    x,y = map(int, input().split())
    perPrices.append(x/y)
    
ans = round(min(perPrices) * 1000, 2)
print(ans)