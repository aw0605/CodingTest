n = int(input())

for i in range(n):
    k, s = input().split(" ")
    ans = ""
    for v in s: ans += v * int(k)
    print(ans)
    
    
