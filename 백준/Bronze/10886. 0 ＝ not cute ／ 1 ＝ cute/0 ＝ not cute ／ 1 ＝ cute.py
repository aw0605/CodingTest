n = int(input())

t,f = 0,0
for _ in range(n):
    o = int(input())
    if o: t += 1
    else: f += 1
        
print("Junhee is cute!" if t > f else "Junhee is not cute!")