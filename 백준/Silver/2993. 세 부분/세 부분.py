w = input()

ans = w
for i in range(1, len(w)):
    for j in range(i+1, len(w)):
        ans = min(ans, w[:i][::-1]+w[i:j][::-1]+w[j:][::-1])
        
print(ans)