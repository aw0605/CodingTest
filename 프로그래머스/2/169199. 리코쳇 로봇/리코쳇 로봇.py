def solution(board):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    robot_pos = None
    target_pos = None
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R': robot_pos = (i, j)
            elif board[i][j] == 'G': target_pos = (i, j)

    queue = [(robot_pos, 0)]
    visited = set()
    visited.add(robot_pos)
    while queue:
        curr_pos, move_count = queue.pop(0)
        if curr_pos == target_pos: return move_count
        for dx, dy in directions:
            x, y = curr_pos
            while 0 <= x+dx < len(board) and 0 <= y+dy < len(board[0]) and board[x+dx][y+dy] != 'D':
                x += dx
                y += dy
            if (x, y) not in visited:
                visited.add((x, y))
                queue.append(((x, y), move_count + 1))

    return -1 