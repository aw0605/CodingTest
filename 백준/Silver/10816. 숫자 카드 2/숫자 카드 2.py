import sys
input = sys.stdin.readline

n = int(input())
have = input().split()
m = int(input())
cards = input().split()

dic = {}
for v in have:
    if dic.get(v): dic[v] += 1
    else: dic[v] = 1
        
ans = [str(dic.get(card, 0)) for card in cards]
    
print(" ".join(ans))

