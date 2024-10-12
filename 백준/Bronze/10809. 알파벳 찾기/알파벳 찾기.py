import sys

s = sys.stdin.readline().strip()
alphabet ='abcdefghijklmnopqrstuvwxyz'

for v in alphabet:
    print(s.index(v) if v in s else -1, end=" ")
