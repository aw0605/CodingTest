a,b,c = map(int, input().split())
arr = sorted([a,b,c])

rest = arr[0] + arr[1]
maxL = min(arr[2], rest-1)

print(rest + maxL)
