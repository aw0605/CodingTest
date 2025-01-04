num = int(input())

ans = 0
for n in range(1,num+1):
    for v in str(n):
        if v == "3" or v == "6" or v == "9": ans += 1
            
print(ans)