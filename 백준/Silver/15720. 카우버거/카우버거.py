import sys
input = sys.stdin.readline

b,c,d = map(int, input().split())
burger = sorted(list(map(int, input().split())), reverse=True)
side = sorted(list(map(int, input().split())), reverse=True)
drink = sorted(list(map(int, input().split())), reverse=True)

setCnt = min(b,c,d)
ans = 0
for i in range(setCnt):
    ans += (burger[i] + side[i] + drink[i]) * 0.9
    
ans += sum(burger[setCnt:]) + sum(side[setCnt:]) + sum(drink[setCnt:])
    
print(sum(burger) + sum(side) + sum(drink))
print(int(ans))