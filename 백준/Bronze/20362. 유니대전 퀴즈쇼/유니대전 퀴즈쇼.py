import sys
input = sys.stdin.readline

n,s = input().strip().split()
n = int(n)

ans = ""
arr = []
for _ in range(n):
    nick, text = input().strip().split()
    arr.append([nick,text])
    if nick == s: ans = text
        
cnt = 0
for nick,text in arr:
    if nick == s: break
    if text == ans: 
        cnt += 1
        
print(cnt)