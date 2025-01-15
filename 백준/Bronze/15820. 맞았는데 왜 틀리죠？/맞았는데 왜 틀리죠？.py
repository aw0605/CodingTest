import sys
input = sys.stdin.readline

s1,s2 = map(int, input().split())

r1,r2 = 0,0
for _ in range(s1):
    a,c = map(int, input().split())
    if a != c:
        print("Wrong Answer")
        break
    else: r1 += 1
        
for _ in range(s2):
    a,c = map(int, input().split())
    if a != c:
        print("Why Wrong!!!")
        break
    else: r2 += 1
        
if r1 == s1 and r2 == s2: print("Accepted")