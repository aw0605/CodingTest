import sys
input = sys.stdin.readline

n,weights = int(input()),list(map(int,input().split()))
m,beads = int(input()),list(map(int,input().split()))

dp = [[0 for j in range((i+1)*500+1)] for i in range(n+1)]
res = []

def cal(num,w):
    if num > n: return 
    if dp[num][w]: return
    
    dp[num][w] = 1
    
    cal(num+1, w)
    cal(num+1, w+weights[num-1])
    cal(num+1, abs(w-weights[num-1]))
    
cal(0,0)

for b in beads:
    if b > 15000:
        res.append("N")
        continue
    if dp[n][b] == 1: res.append("Y")
    else: res.append("N")
        
print(*res)