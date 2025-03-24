A,B = input(), input()
hint = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

arr = []
for i in range(len(A)):
    arr.append(hint[ord(A[i]) - 65])
    arr.append(hint[ord(B[i]) - 65])
    
while len(arr) > 2:
    res = []
    for i in range(1, len(arr)):
        res.append((arr[i-1] + arr[i]) % 10)
    arr = res
    
print(str(arr[0])+str(arr[1]))