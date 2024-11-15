import sys
input = sys.stdin.readline

s = input().strip()
n = int(input())

count = [[0] * 26]

for i, v in enumerate(s):
    count.append(count[len(count) - 1][:])
    count[i + 1][ord(v) - 97] += 1
    
for _ in range(n):     
    alpha, l, r = input().strip().split()     
    ans = count[int(r) + 1][ord(alpha) - 97] - count[int(l)][ord(alpha) - 97]     
    print(ans)