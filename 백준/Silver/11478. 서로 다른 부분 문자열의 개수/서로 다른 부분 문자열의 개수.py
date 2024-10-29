s = input()
ans = {}
k = len(s)

for i in range(k):
    for j in range(k-i):
        ans[s[j:j+i+1]] = 1
    
print(len(ans))