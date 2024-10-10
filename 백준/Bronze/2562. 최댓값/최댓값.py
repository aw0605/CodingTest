import sys

arr = []

for i in range(9):
    n = int(sys.stdin.readline())
    arr.append(n)

max_num = max(arr)
max_idx = arr.index(max_num) + 1

print(max_num)
print(max_idx)