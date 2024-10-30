from math import lcm
import sys
data = sys.stdin.read().split()

n = int(data[0])

ans = []

for i in range(n):
    a,b = map(int, data[2*i+1:2*i+3])
    ans.append(str(lcm(a,b)))
    
print("\n".join(ans))    