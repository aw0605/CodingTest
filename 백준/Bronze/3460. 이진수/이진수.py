import sys
input = sys.stdin.readline

def findIdx(v):
    arr = []
    for i,s in enumerate(v):
        if s == "1": arr.append(i)
    return arr

t = int(input())
for _ in range(t):
    n = bin(int(input()))[2:][::-1]
    ans = findIdx(n)
    print(" ".join(map(str, ans)))