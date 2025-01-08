import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h,m,a,d,ah,am,aa,ad = map(int, input().split())
    hp = h + ah if h + ah > 1 else 1
    mp = m + am if m + am > 1 else 1
    attack = a + aa if a + aa > 0 else 0
    defense = d + ad
    total = hp + (5*mp) + (2*attack) + (2*defense)
    print(total)