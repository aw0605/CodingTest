import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
sort_arr = sorted(set(arr))

dic = {v:i for i, v in enumerate(sort_arr)}

print(" ".join(map(str, [dic[v] for v in arr])))