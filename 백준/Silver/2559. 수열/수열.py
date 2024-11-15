import sys
input = sys.stdin.readline

n,k = map(int, input().split())
arr = list(map(int, input().split()))

sum_prev = sum(arr[:k])
answer = sum_prev

for i in range(n-k) :
    sum_prev += arr[i+k] - arr[i]
    answer = max(sum_prev, answer)

print(answer)