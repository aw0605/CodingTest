import sys
input = sys.stdin.readline

n = int(input())
a = {int(num): 1 for num in input().split()} 
m = int(input())
b = list(map(int, input().split()))

for num in b:
    print(a.get(num, 0))