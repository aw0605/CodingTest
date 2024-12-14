import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

arr = []
while True:
    try: arr.append(int(input()))
    except: break

def sol(arr):
    if len(arr) == 0: return
    l, r = [], []
    mid = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > mid:
            l = arr[1:i]
            r = arr[i:]
            break
    else: l = arr[1:]
    
    sol(l)
    sol(r)
    print(mid)

sol(arr)