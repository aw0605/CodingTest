import sys
input = sys.stdin.readline

r, c = map(int, input().split())
arr = []
for i in range(r):
    row = input().strip()
    arr.append(row + row[::-1])
arr += arr[::-1]

a, b = map(int, input().split())
if arr[a-1][b-1] == "#": arr[a-1] = arr[a-1][:b-1] + "." + arr[a-1][b:]
else: arr[a-1] = arr[a-1][:b-1] + "#" + arr[a-1][b:]

for row in arr:print(row)