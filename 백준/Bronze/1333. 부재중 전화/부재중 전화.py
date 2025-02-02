n, l, d = map(int, input().split())

time = [1] * (n*l + ((n-1)*5))
for i in range(n):
    start = (l+5) * i
    for j in range(start, start+l): time[j] = 0
        
cur = 0
while cur < len(time):
    if time[cur]: break
    cur += d
    
print(cur)