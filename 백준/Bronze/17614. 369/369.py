num = int(input())

ans = 0
for n in range(1, num+1):
    ans += str(n).count('3')+str(n).count('6')+str(n).count('9')
print(ans)