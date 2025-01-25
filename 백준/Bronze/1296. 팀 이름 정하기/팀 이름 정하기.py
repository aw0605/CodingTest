import sys
input = sys.stdin.readline

y = input().strip()
n = int(input())
arr = [input().strip() for _ in range(n)]

def calc(y,t):
    s = y + t
    L = s.count("L")
    O = s.count("O")
    V = s.count("V")
    E = s.count("E")
    return ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
    
res = []
for t in arr:
    score = calc(y,t)
    res.append((t,score))
    
res.sort(key=lambda x: (-x[1],x[0]))
print(res[0][0])