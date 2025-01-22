a = input()
b = input()

ab = ""
for i in range(8):
    ab += a[i] + b[i]
    
while len(ab) > 2:
    tmp = ""
    for i in range(len(ab) - 1):
        tmp += str((int(ab[i]) + int(ab[i+1])) % 10)
    ab = tmp
    
print(ab)