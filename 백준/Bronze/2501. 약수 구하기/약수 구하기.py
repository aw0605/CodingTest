n,k = map(int, input().split())
arr = set()

for i in range(1, int(n**0.5)+1):
    if n % i == 0: 
        arr.add(i)
        arr.add(n//i)
        
arr = sorted(arr)
        
print(0 if k > len(arr) else arr[k-1])