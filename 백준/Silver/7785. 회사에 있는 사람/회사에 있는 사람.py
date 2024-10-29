import sys
input = sys.stdin.readline

n = int(input())
cur = set()

for _ in range(n):
    name, status = input().split()
    if status == "enter": cur.add(name)
    elif status == "leave": cur.discard(name)
        
ans = sorted(cur, reverse=True)

print('\n'.join(ans))