import sys
input = sys.stdin.read

def canto(n):
    if n == 0: return "-"
    arr = canto(n-1)
    return arr + " "*len(arr) + arr 
    
data = list(map(int,input().split()))
        
for n in data:
    print(canto(n))