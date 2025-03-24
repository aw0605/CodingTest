hint = {"A": 3, "B": 2, "C": 1, "D": 2, "E": 3, "F": 3, "G": 2, "H": 3, "I": 3, "J": 2, "K": 2, "L": 1, "M": 2, "N": 2, "O": 1, "P": 2, "Q": 2, "R": 2, "S": 1, "T": 2, "U": 1, "V": 1, "W": 1, "X": 2, "Y": 2, "Z": 1}
A,B = input(), input()

arr = []
for i in range(len(A)):
    arr.append(hint[A[i]])
    arr.append(hint[B[i]])
    
while len(arr) > 2:
    arr = [(arr[i] + arr[i+1]) % 10 for i in range(len(arr)-1)]
    
print(str(arr[0])+str(arr[1]))