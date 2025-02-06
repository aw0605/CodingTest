import sys
input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]
for i in range(n):
    row = arr[i]
    col = ""
    for j in range(n): col += arr[j][i]
    if row != col:
        print("NO")
        exit()
        
print("YES")