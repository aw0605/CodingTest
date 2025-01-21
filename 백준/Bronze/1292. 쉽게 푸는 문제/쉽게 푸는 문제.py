import sys
input = sys.stdin.readline

a,b = map(int, input().split())
arr = [0]
for i in range(1,(b+1)//2+1):
    arr.extend([i] * i)

print(sum(arr[a:b+1]))