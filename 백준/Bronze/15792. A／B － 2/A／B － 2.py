a,b = map(int, input().split())

res = (str(a//b)+".")
a = (a%b) * 10
for _ in range(1000):
    res += str(a//b)
    a = (a%b) * 10
    
print(res)