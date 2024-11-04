import sys
input = sys.stdin.readline

n = int(input())
ans = set()
ans.add("ChongChong")

for _ in range(n):
    cur, meet = input().split()
    if cur in ans:
        ans.add(meet)
    if meet in ans:
        ans.add(cur)
        
print(len(ans))