import sys
input = sys.stdin.readline

n = int(input())
print("int a;")
print("int *ptr = &a;")
for i in range(2,n+1):
    if i == 2: print("int **ptr2 = &ptr;")
    else: print(f"int {'*'*i}ptr{i} = &ptr{i-1};")