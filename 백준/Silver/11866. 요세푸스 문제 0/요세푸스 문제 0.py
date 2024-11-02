import sys
input = sys.stdin.readline

n,k = map(int, input().split())
q = [i+1 for i in range(n)]
    
point = 0

print("<",end="")

while len(q) > 1:
    point = (point + k - 1) % n
    print(str(q.pop(point))+",", end=" ")
    n -= 1

print(str(q[0])+">")