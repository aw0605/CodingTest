arr = [list(map(int, input().split())) for _ in range(9)]
ans = {}

for i in range(9):
    maxN = max(arr[i])
    j = arr[i].index(maxN)
    ans[maxN] = [i+1,j+1]

maxV = max([v for v in ans.keys()])

print(maxV)
print(ans[maxV][0], ans[maxV][1])
    
        