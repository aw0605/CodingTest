import sys
input = sys.stdin.readline

arr = set()
for _ in range(2):
    p = input().strip().split()
    for color in p: arr.add(color)
            
sorted_arr = sorted(list(arr))

for i in sorted_arr:
    for j in sorted_arr:
        print(i,j)