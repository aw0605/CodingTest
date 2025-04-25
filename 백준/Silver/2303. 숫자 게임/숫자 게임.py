import sys
input = sys.stdin.readline

n = int(input())
maxArr = [0] * n

for i in range(n):
    cards = list(map(int, input().split()))
    for j in range(5):
        for k in range(j+1, 5):
            for l in range(k+1, 5):
                res = (cards[j] + cards[k] + cards[l]) % 10
                if maxArr[i] < res: maxArr[i] = res 

maxN = max(maxArr)
for i in range(n-1, -1, -1):
    if maxArr[i] == maxN:
        print(i + 1)
        break