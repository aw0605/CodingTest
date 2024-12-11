import sys
input = sys.stdin.readline

s1,s2 = [0] + list(input().strip()), [0] + list(input().strip())
l1, l2 = len(s1), len(s2)

arr = [['' for _ in range(l1)] for _ in range(l2)]

for i in range(1, l2):
    for j in range(1, l1):
        if s1[j] == s2[i]: arr[i][j] = arr[i-1][j-1] + s1[j]
        else:
            if len(arr[i][j-1]) > len(arr[i-1][j]): arr[i][j] = arr[i][j-1]
            else: arr[i][j] = arr[i-1][j]

ans = len(arr[-1][-1])

print(ans)
if ans != 0:
    print(arr[-1][-1])