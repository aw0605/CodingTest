from collections import deque

def solution(info, edges):
    answer = 0
    n = len(info)
    tree = {i: [] for i in range(n)}
    for p, s in edges: tree[p].append(s)
    q = deque([[0, tree[0], 1, 0]])
    
    while q:
        now, can_move, sheep, wolf = q.popleft()
        if answer < sheep: answer = sheep
        for i, node in enumerate(can_move):
            if info[node] == 1:
                if sheep > wolf + 1:
                    q.append([node, can_move[:i] + can_move[i + 1:] + tree[node], sheep, wolf + 1])
            else:
                q.append([node, can_move[:i] + can_move[i + 1:] + tree[node], sheep + 1, wolf])

    return answer