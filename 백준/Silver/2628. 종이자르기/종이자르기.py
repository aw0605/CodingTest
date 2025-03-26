import sys
input = sys.stdin.readline

w,h = map(int, input().split())
n = int(input())

wArr = [0,w]
hArr = [0,h]
for _ in range(n):
    a,b = map(int, input().split())
    if a: wArr.append(b)
    else: hArr.append(b)
        
wArr.sort()
hArr.sort()

ans = 0
 
for i in range(len(wArr)-1):
    for j in range(len(hArr)-1):
        r = wArr[i+1] - wArr[i]
        c = hArr[j+1] - hArr[j]
        ans = max(ans, r*c)

print(ans)