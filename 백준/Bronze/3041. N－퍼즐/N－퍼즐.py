import sys
input = sys.stdin.readline

ans = ["ABCD", "EFGH", "IJKL", "MNO."]
arr = [input().strip() for _ in range(4)]
diff = {}
dist = 0
for i in range(4):
    for j in range(4):
        if ans[i][j] != arr[i][j] and arr[i][j] != ".": 
            diff[arr[i][j]] = (i,j)
            
for i in range(4):
    for j in range(4):
        if ans[i][j] in diff:
            dist += abs(diff[ans[i][j]][0] - i) + abs(diff[ans[i][j]][1] - j)
            
print(dist)