N,B = input().split()
nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = 0

for i,v in enumerate(N[::-1]):
    ans += (int(B) ** i) * nums.index(v)
    
print(ans)

