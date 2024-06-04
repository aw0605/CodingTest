def solution(board, moves):
    answer = 0
    dolls = []
    
    for j in moves:
        for i in range(len(board)):
            doll = board[i][j-1]
            if doll != 0:
                if dolls and dolls[-1] == doll:
                    answer += 2
                    dolls.pop()
                else: dolls.append(doll)
                board[i][j-1] = 0
                break

    return answer