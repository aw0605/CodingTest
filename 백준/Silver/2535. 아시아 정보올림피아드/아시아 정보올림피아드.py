import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: -x[2])

cnt = 0
print(arr[0][0], arr[0][1])
print(arr[1][0], arr[1][1])
if arr[0][0] == arr[1][0]: cnt = 1

for i in range(2,n):
    if not cnt:
        print(arr[i][0], arr[i][1])
        break
    else:
        if arr[1][0] != arr[i][0]:
            print(arr[i][0], arr[i][1])
            break