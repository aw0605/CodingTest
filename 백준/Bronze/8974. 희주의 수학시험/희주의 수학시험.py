a,b = map(int, input().split())

arr = []
for i in range(1, b+1):
    arr.extend([i] * i)
    
print(sum(arr[a-1:b]))