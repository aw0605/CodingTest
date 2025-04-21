import sys
input = sys.stdin.readline

p = int(input())
for _ in range(p):
    data = list(map(int, input().split()))
    t, arr = data[0], data[1:]
    cnt = 0
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                cnt += 1
                arr[i],arr[j] = arr[j],arr[i]
                
    print(t, cnt)