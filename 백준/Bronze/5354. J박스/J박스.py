import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1: print('#')
    else:
        print('#'*n)
        for _ in range(n-2): print('#'+'J'*(n-2)+'#')
        print('#'*n)
    print()