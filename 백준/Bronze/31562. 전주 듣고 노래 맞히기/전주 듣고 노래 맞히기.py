import sys
input = sys.stdin.readline

n,m = map(int, input().split())
song = {}
for _ in range(n):
    t,s,*a = input().strip().split()
    song[s] = a[:3]
    
for _ in range(m):
    b = input().strip().split()
    cnt = 0
    t = ""
    for s in song:
        if b == song[s]:
            cnt += 1
            t = s
    if cnt > 1: print("?")
    elif cnt == 1: print(t)
    else: print("!")