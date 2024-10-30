import sys
data = sys.stdin.read().splitlines()

def isPrime(x):
    if x <= 1: return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0: return False
    return True

t = int(data[0])
ans = []

for i in range(1,t+1):
    n = int(data[i])
    while not isPrime(n):
        n += 1
    ans.append(str(n))

print("\n".join(ans))
