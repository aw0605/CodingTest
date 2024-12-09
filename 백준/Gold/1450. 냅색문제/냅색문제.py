import bisect
import sys
input = sys.stdin.readline

n,c = map(int,input().split())

weights = list(map(int,input().split()))
w1,w2 = weights[:n//2],weights[n//2:]
sum1,sum2 = [],[]

def bf(w,s,i,t):
    if len(w) == i:
        s.append(t)
        return s
    bf(w,s,i+1,t)
    bf(w,s,i+1,t+w[i])
    return s

sum1 = bf(w1,sum1,0,0)
sum2 = sorted(bf(w2,sum2,0,0))

ans = 0

for v in sum1:
    if c < v: continue
    i = bisect.bisect_right(sum2,c-v)
    ans += i
    
print(ans)