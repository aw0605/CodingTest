import sys
input = sys.stdin.readline

hint = {"A": 3, "B": 2, "C": 1, "D": 2, "E": 4, "F": 3, "G": 1, "H": 3, 
        "I": 1, "J": 1, "K": 3, "L": 1, "M": 3, "N": 2, "O": 1, "P": 2, 
        "Q": 2, "R": 2, "S": 1, "T": 2, "U": 1, "V": 1, "W": 1, "X": 2, "Y": 2, "Z": 1}

n,m = map(int, input().split())
a,b = input().strip().split()

minL = min(n,m)
s = ""
for i in range(minL):
    s += a[i] + b[i]
s += a[minL:] + b[minL:]
    
arr = [hint[v] for v in s]
while len(arr) > 2:
    arr = [(arr[i] + arr[i+1]) % 10 for i in range(len(arr) - 1)]
    
if arr[0] == 0: print(f"{arr[1]}%")
else: print(f"{arr[0]}{arr[1]}%")