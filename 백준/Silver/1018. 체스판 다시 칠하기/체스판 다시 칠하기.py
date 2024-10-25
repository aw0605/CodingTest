n, m = map(int,input().split())

board = []
ans = []

for i in range(n):
    board.append(input())
    
for a in range(n-7):
    for b in range(m-7):
        w_index=0
        b_index=0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j)%2 == 0:
                    if board[i][j]!='W': w_index += 1
                    else: b_index+=1
                else:
                    if board[i][j]!='W': b_index += 1
                    else: w_index += 1
                        
        ans.append(w_index)
        ans.append(b_index)
        
print(min(ans))