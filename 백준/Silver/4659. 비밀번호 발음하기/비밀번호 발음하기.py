import sys
input = sys.stdin.readline

while True:
    cur = input().strip()
    if cur == 'end': break
    
    vowels = 'aeiou'
    accept = True  
    
    if not any(v in cur for v in vowels): accept = False
    
    vCnt, cCnt = 0, 0
    for i in cur:
        if i in vowels:
            vCnt += 1
            cCnt = 0
        else:
            vCnt = 0
            cCnt += 1

        if vCnt == 3 or cCnt == 3:
            accept = False
            break
    
    for i in range(1, len(cur)):
        if cur[i] == cur[i-1] and cur[i] not in ['e', 'o']:
            accept = False
            break
    
    print(f'<{cur}> is acceptable.' if accept else f'<{cur}> is not acceptable.')