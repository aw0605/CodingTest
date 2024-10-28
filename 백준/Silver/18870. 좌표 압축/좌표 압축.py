import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
sort_arr = sorted(set(arr))

dic = {sort_arr[i]:i for i in range(len(sort_arr))}

for v in arr:
    print(dic[v], end=" ")