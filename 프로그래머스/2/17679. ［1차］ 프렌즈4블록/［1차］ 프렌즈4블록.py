def solution(m, n, board):
    b = [list(v) for v in board]
    answer = 0
    point = 1
    
    while point != 0:
        pop = []
        point = 0

        for i in range(m - 1):
            for j in range(n - 1):
                if b[i][j] == b[i][j + 1] == b[i + 1][j] == b[i + 1][j + 1] != '팡!':
                    pop.append((i, j))
                    point += 1

        for i, j in pop:
            b[i][j] = b[i][j + 1] = b[i + 1][j] = b[i + 1][j + 1] = '팡!'

        for j in range(n):
            for i in range(m - 1, 0, -1):
                if b[i][j] == '팡!':
                    for k in range(i - 1, -1, -1):
                        if b[k][j] != '팡!':
                            b[i][j], b[k][j] = b[k][j], '팡!'
                            break

    for v in b: answer += v.count('팡!')

    return answer