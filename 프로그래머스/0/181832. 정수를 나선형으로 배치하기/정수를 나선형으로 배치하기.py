def solution(n):
    arr = [[0] * n for _ in range(n)]
    x, y = 0, 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direction = 0
    num = 1

    while num <= n**2:
        arr[x][y] = num
        num += 1
        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
            x, y = nx, ny
        else:
            direction = (direction + 1) % 4
            x, y = x + dx[direction], y + dy[direction]

    return arr