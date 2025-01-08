import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    print(f"Pairs for {n}:", end=' ')
    for i in range(1, n//2+1):
        if i < n-i:
            if i != 1: print(',', end=' ')
            print(i, n-i, end='')
    print()