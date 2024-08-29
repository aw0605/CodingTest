def solution(n):
    answer = 0
    NOT = 100
    status = [NOT] * n

    def is_available(status, row, col):
        if status[col] != NOT:
            return False
        for idx in range(len(status)):
            if status[idx] != NOT and abs((row - status[idx]) / (col - idx)) == 1: return False
        return True

    def dfs(n, row, status):
        nonlocal answer
        if row == n:
            answer += 1
            return
        for col in range(n):
            if is_available(status, row, col):
                status[col] = row
                dfs(n, row + 1, status)
                status[col] = NOT

    dfs(n, 0, status)

    return answer
