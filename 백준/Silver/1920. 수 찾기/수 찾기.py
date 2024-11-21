import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))
a.sort()

for num in arr:
    s, e = 0, n - 1
    find = False

    while s <= e:
        mid = (s + e) // 2
        if num == a[mid]:
            find = True
            print(1)
            break
        elif num > a[mid]: s = mid + 1
        else: e = mid - 1

    if not find: print(0)