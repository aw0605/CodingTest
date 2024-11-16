import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key = lambda x: (x[1], x[0]))

count = 0
end = 0

for s,e in arr:
    if end <= s:
        count += 1
        end = e
        
print(count)