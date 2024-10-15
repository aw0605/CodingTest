n,m = map(int,input().split())
arr1 = []
arr2 = []
ans = [[0] * m for _ in range(n)]

for i in range(n*2):
    arr = list(map(int, input().split()))
    if i < n: arr1.append(arr)
    else: arr2.append(arr)

for i in range(n):
    for j in range(m):
        ans[i][j] = arr1[i][j] + arr2[i][j]
        
for i in range(n):
    for j in range(m):
        print(ans[i][j], end=" ")
    print()