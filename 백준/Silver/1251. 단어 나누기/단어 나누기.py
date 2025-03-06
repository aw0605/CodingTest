w = list(input())
ans = []

for i in range(1, len(w) - 1):
    for j in range(i+1, len(w)):
        a,b,c = w[:i],w[i:j],w[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        ans.append("".join(a+b+c))
        
print(sorted(ans)[0])