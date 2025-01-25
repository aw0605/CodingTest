import sys
input = sys.stdin.readline

l = int(input())
n = int(input())

roll = [0] * l
cnt = [0] * (n+1)
maxG = [0,0]
for i in range(1,n+1):
    s,e = map(int, input().split())
    guess = e - s + 1
    if maxG[0] < guess: maxG = [guess, i]
    for j in range(s,e+1):
        if not roll[j-1]: 
            roll[j-1] = i
            cnt[i] += 1
            
print(maxG[1])
print(cnt.index(max(cnt)))