arr = list(map(int, input().split()))

while arr != sorted(arr):
    for i in range(4):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(" ".join(map(str, arr)))