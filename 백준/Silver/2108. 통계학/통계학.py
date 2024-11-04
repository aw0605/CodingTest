from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

counter = Counter(arr).most_common()
max_fre = counter[0][1]
modes = [v for v,f in counter if f == max_fre]
modes.sort()

print(round(sum(arr)/n))
print(arr[n//2])
print(modes[0] if len(modes) == 1 else modes[1])
print(max(arr) - min(arr))