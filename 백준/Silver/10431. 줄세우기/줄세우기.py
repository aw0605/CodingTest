import sys
input = sys.stdin.readline

p = int(input())
for _ in range(p):
    data = list(map(int, input().split()))
    t, arr = data[0], data[1:]
    cnt = 0
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] > arr[i]: cnt += 1
                
    print(t, cnt)