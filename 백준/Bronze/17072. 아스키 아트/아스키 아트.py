import sys
input = sys.stdin.readline

def intensity(r, g, b):
    i = 2126 * r + 7152 * g + 722 * b
    if 0 <= i < 510000: return "#"
    elif 510000 <= i < 1020000: return "o"
    elif 1020000 <= i < 1530000: return "+"
    elif 1530000 <= i < 2040000: return "-"
    elif 2040000 <= i: return "."

n, m = map(int, input().split())
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(0, len(row), 3):
        r, g, b = row[j], row[j+1], row[j+2]
        print(intensity(r, g, b), end="")
    print()