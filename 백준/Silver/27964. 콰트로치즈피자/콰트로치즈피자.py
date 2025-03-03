import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().strip().split())

cheese = []
for v in arr:
    if v[-6:] == "Cheese" and v not in cheese: cheese.append(v)
    
print ("yummy" if len(cheese) >= 4 else "sad")