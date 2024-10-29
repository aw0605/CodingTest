from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
have = list(map(int, input().split()))
have_dic = defaultdict(int)
for v in have:
    have_dic[v] += 1

m = int(input())
cards = list(map(int, input().split()))

ans = []
for card in cards:
    ans.append(str(have_dic.get(card, 0)))
    
print(" ".join(ans))

