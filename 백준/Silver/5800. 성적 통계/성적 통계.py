import sys
input = sys.stdin.readline

k = int(input())
for i in range(1,k+1):
    print(f"Class {i}")
    n, *arr = map(int, input().split())
    arr.sort(reverse = True)
    diff = 0
    for i in range(n-1):
        diff = max(diff, arr[i] - arr[i+1])
    print(f"Max {arr[0]}, Min {arr[-1]}, Largest gap {diff}")