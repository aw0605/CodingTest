import sys
input = sys.stdin.readline

s = input().strip().split('-')

addnums = []

for v in s:
    num = 0
    for n in v.split('+'): num += int(n)
    addnums.append(num)
    
ans = addnums[0]
for i in addnums[1:]:
    ans -= i
    
print(ans)