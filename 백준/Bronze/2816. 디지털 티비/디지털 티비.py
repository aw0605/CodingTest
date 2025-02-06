import sys
input = sys.stdin.readline

n = int(input())
channel = [input().strip() for _ in range(n)]

i1,i2 = channel.index("KBS1"), channel.index("KBS2")
if i1 > i2: i2 += 1
    
print("1"*i1 + "4"*i1 + "1"*i2 + "4"*(i2-1))