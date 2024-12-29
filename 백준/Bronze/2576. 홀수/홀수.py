arr = []
for _ in range(7):
    n = int(input())
    if n % 2: arr.append(n)
        
if not len(arr): print(-1)
else:
    print(sum(arr))
    print(min(arr))