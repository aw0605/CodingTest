import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    arr = input().strip().split()
    ans = "god"
    for i in range(1,len(arr)):
        ans += arr[i]
    print(ans)