a, b, c = [int(input()) for _ in range(3)]

if a == b == c and a == 60: print("Equilateral")
elif a + b + c == 180:
    if a != b and b != c and a != c: print("Scalene")
    else: print("Isosceles")
else: print("Error")
