import sys
input = sys.stdin.readline

score = [100,100,200,200,300,300,400,400,500]
arr = list(map(int, input().split()))

res = 0
for i in range(9):
    if arr[i] > score[i]: 
        print("hacker")
        exit()
    else:
        res += arr[i]
        if res >= 100: 
            print("draw")
            exit()

print("none")