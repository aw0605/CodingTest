import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    name, d,m,y = input().strip().split()
    d,m,y = map(int, [d,m,y])
    arr.append([y,m,d,name])
    
arr.sort()
print(arr[-1][3])
print(arr[0][3])