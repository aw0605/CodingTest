ans = [0,0]

for i in range(1,6):
    score = sum(list(map(int, input().split())))
    if ans[1] < score:
        ans[0] = i
        ans[1] = score  

print(ans[0], ans[1])