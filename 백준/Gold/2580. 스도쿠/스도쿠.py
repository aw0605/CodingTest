import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
empty_pos = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

rows = [[False] * 10 for _ in range(9)]
cols = [[False] * 10 for _ in range(9)]
boxes = [[False] * 10 for _ in range(9)]

for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            num = board[i][j]
            rows[i][num] = True
            cols[j][num] = True
            boxes[(i // 3) * 3 + (j // 3)][num] = True

def dfs(depth):
    if depth == len(empty_pos): return True
    
    x, y = empty_pos[depth]
    box_index = (x // 3) * 3 + (y // 3)
    
    for num in range(1, 10):
        if not rows[x][num] and not cols[y][num] and not boxes[box_index][num]:
            board[x][y] = num
            rows[x][num] = True
            cols[y][num] = True
            boxes[box_index][num] = True

            if dfs(depth + 1): return True

            board[x][y] = 0
            rows[x][num] = False
            cols[y][num] = False
            boxes[box_index][num] = False
    return False

dfs(0)

for row in board:
    print(*row)