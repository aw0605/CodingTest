import sys
input = sys.stdin.readline

i = 0
while True:
    a,b = input().strip(), input().strip()
    if a == "END": break
    i += 1
    if sorted(a) == sorted(b): print(f"Case {i}: same")
    else: print(f"Case {i}: different")