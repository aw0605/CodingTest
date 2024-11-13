import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
reverse_arr = arr[::-1]

inc = [1] * n
dec = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            inc[i] = max(inc[i], inc[j] + 1)
        if reverse_arr[i] > reverse_arr[j]:
            dec[i] = max(dec[i], dec[j] + 1)
            
dec = dec[::-1]

res = [0] * n
for i in range(n):
    res[i] = inc[i] + dec[i] - 1
    
print(max(res))