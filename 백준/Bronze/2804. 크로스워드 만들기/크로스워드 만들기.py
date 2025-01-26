import sys
input = sys.stdin.readline

a,b = input().strip().split()

l = len(a)
for i,s in enumerate(a):
    if s in b:
        al = i
        bl = b.index(s)
        break
        
for i in range(len(b)):
    if i == bl:
        print(a)
    else:
        print("." * al + b[i] + "." * (l-1-al))