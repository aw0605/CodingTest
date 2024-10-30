import sys
data = sys.stdin.read().split()

def GCD(x,y):
    while (y):
        x, y = y, x%y
    return x

def LCM(x,y):
    return (x*y)//GCD(x,y)

n = int(data[0])

ans = []

for i in range(n):
    a,b = map(int, data[2*i+1:2*i+3])
    ans.append(str(LCM(a,b)))
    
print("\n".join(ans))    