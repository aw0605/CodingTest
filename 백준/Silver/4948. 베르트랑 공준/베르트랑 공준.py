ans = [0] * 2 + [1] * 246912
    
for i in range(2, int(246913**0.5) + 1):
    if ans[i]:
        for j in range(i * i, 246913, i):
            ans[j] = 0

while True:
    n = int(input())
    if n == 0: break
    print(sum(ans[n+1:n*2+1]))