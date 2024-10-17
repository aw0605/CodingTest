n = int(input())
num = 1
ans = 1

while n > num:
    num += 6 * ans
    ans += 1
    
print(ans)