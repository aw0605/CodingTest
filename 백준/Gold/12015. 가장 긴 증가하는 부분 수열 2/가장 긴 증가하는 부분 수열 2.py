import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

lis = [0]

def binary(num):
    s, e = 0, len(lis)
    while s <= e:
        mid = (s+e) // 2
        if lis[mid] < num: s = mid + 1
        else: e = mid - 1
    return s
            
for num in arr:
    if lis[-1] < num: lis.append(num)
    else:
        i = binary(num)
        lis[i] = num
        
print(len(lis) - 1)