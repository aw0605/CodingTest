n = int(input())
cur = 666
i = 0

while True:
    if '666' in str(cur): i += 1
    if i == n:
        print(cur)
        break
    cur += 1
    
    