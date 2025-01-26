import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr == [-1]: break
    res = set()
    for n in arr[:-1]:
        if 2*n in arr: res.add(n)
    print(len(res))