def get_next_positions(board, loc):
    dRow, dCol = [0, 0, 1, -1], [1, -1, 0, 0]
    next_positions = []
    for d in range(4):
        nr, nc = loc[0] + dRow[d], loc[1] + dCol[d]
        if nr < 0 or nc < 0 or nr >= len(board) or nc >= len(board[0]): continue
        elif board[nr][nc] == 0: continue
        next_positions.append((nr, nc))
    return next_positions


def search(board, aloc, bloc, turn):
    if turn % 2 == 0: next_positions = get_next_positions(board, aloc)
    else: next_positions = get_next_positions(board, bloc)
    if not next_positions: return turn % 2 != 0, turn
    if aloc == bloc: return turn % 2 == 0, turn + 1

    win, lose = [], []
    if turn % 2 == 0:
        board[aloc[0]][aloc[1]] = 0
        for nr, nc in next_positions:
            is_a_win, cnt = search(board, [nr, nc], bloc, turn + 1)
            if is_a_win: win.append(cnt)
            else: lose.append(cnt)
        board[aloc[0]][aloc[1]] = 1
    else:
        board[bloc[0]][bloc[1]] = 0
        for nr, nc in next_positions:
            is_a_win, cnt = search(board, aloc, [nr, nc], turn + 1)
            if not is_a_win: win.append(cnt)
            else: lose.append(cnt)
        board[bloc[0]][bloc[1]] = 1

    if win: return turn % 2 == 0, min(win)
    else: return turn % 2 != 0, max(lose)


def solution(board, aloc, bloc):
    winner, answer = search(board, aloc, bloc, 0)
    return answer