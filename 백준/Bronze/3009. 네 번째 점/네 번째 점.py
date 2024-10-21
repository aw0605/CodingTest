xArr = []
yArr = []

for _ in range(3):
    x,y = map(int, input().split())
    xArr.append(x)
    yArr.append(y)
    
for i in range(3):
    if xArr.count(xArr[i]) == 1: ansX = xArr[i]
    if yArr.count(yArr[i]) == 1: ansY = yArr[i]
        
print(ansX, ansY)