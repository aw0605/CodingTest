import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

for i in range(1,n):
    diff = 0
    s1,s2 = s[:i],s[-i:]
    for a,b in zip(s1,s2):
        if a != b: diff += 1
    if diff == 1:
        print("YES")
        exit()
        
print("NO")