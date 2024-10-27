import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
user = defaultdict(list)

for _ in range(n):
    age, name = input().split()
    user[int(age)].append(name)

for age,values in sorted(user.items()):
    for v in values:
        print(age, v)