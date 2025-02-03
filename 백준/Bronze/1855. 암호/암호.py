import sys
input = sys.stdin.readline

r = int(input())
s = input().strip()
c = len(s)//r

ans = ""
arr = [[] for _ in range(r)]
for i in range(1, c+1):
    if i%2:
        for j in range(r):
            arr[j].append(s[j])
    else:
        for j in range(r):
            arr[j].append(s[r-j-1])
    s = s[r:]
    
for row in arr:
    for v in row: ans += v
        
print(ans)