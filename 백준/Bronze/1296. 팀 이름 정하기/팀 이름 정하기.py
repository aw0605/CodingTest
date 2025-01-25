import sys
input = sys.stdin.readline

y = input().strip()
n = int(input())
arr = sorted([input().strip() for _ in range(n)])
maxT = maxI = 0
for i in range(n):
    s = y + arr[i]
    L = s.count("L")
    O = s.count("O")
    V = s.count("V")
    E = s.count("E")
    score = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
    if maxT < score:
        maxT = score
        maxI = i

print(arr[maxI])