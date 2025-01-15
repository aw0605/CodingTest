import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t+1):
    a,b,c = sorted(map(int, input().split()))
    print(f"Case #{i}:", end=" ")
    if a + b <= c: print("invalid!")
    elif a == b == c: print("equilateral")
    elif a == b or a == c or b == c: print("isosceles")
    else: print("scalene")