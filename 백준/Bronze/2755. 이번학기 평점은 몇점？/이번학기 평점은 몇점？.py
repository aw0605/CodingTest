import sys
input = sys.stdin.readline

dic = {
    "A+": 4.3, "A0": 4.0, "A-": 3.7,
    "B+": 3.3, "B0": 3.0, "B-": 2.7,
    "C+": 2.3, "C0": 2.0, "C-": 1.7,
    "D+": 1.3, "D0": 1.0, "D-": 0.7, "F": 0.0
}

n = int(input())

score = total = 0
for _ in range(n):
    sub, s, g = input().strip().split()
    s = int(s)
    total += s
    score += s * dic[g]

ans = round(score/total + 10**-10, 2)
print(f"{ans:.2f}")