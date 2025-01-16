import sys
input = sys.stdin.readline

l = int(input())
s = input().strip()

c2 = s.count("2")
ce = s.count("e")

if c2 > ce: print(2)
elif ce > c2: print("e")
else: print("yee")