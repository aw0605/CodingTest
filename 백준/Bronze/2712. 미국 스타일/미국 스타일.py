import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, unit = input().split()
    n = float(n)
    if unit == "kg": 
        n *= 2.2046
        unit = "lb"
    elif unit == "lb": 
        n *= 0.4536
        unit = "kg"
    elif unit == "l": 
        n *= 0.2642
        unit = "g"
    elif unit == "g": 
        n *= 3.7854
        unit = "l"
    print(f"{n:.4f} {unit}")