import sys
input = sys.stdin.readline

n = int(input())
structure = input().split()
a = input().split()

m = int(input())
b = input().split()

q = [a[i] for i in range(n) if structure[i] == "0"]
q.reverse()

print(" ".join((q+b)[:m]))