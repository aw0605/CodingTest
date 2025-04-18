import sys
input = sys.stdin.readline

n = int(input())
s1, s2 = input().strip(), input().strip() 

if sorted(s1) != sorted(s2):
    print("NO")
    sys.exit()
    
if s1[0] != s2[0] or s1[-1] != s2[-1]:
    print("NO")
    sys.exit()

for s in "aeiou":
    s1 = s1.replace(s, "")
    s2 = s2.replace(s, "")
if s1 != s2:
    print("NO")
    sys.exit()
    
print("YES")