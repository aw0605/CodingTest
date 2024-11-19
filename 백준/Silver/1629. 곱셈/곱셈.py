import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())

def multi(a,b):
    if b == 1: return a % c
    else:
        cur = multi(a,b//2)
        if b % 2 == 0: return (cur * cur) % c
        else: return (cur * cur * a) % c
        
print(multi(a,b))