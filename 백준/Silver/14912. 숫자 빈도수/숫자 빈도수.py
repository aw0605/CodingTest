n,d = map(int, input().split())
d = str(d)
print(sum(str(i).count(d) for i in range(1,n+1)))