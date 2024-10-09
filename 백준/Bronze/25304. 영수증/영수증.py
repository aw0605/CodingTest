import sys

total = int(sys.stdin.readline())
n = int(sys.stdin.readline())
result = 0

for i in range(n):
    price, item = map(int, sys.stdin.readline().split())
    result += price * item
    
print("Yes" if total == result else "No")