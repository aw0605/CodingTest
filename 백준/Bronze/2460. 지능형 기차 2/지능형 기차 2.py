import sys
input = sys.stdin.readline

ans = 0
person = 0
for _ in range(10):
    o, i = map(int, input().split())
    person += i - o
    ans = max(ans, person)
    
print(ans)    