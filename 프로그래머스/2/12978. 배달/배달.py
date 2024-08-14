def solution(N, road, K):
    visited = [False] * (N + 1)
    costs = [float('inf')] * (N + 1)
    costs[1] = 0
    parents = [1]
    
    while (parents):
        parent = parents.pop(0)
        visited[parent] = True
        for a, b, cost in road:
            if (a == parent or b == parent):
                target = b if a == parent else a
                if costs[target] > costs[parent] + cost:
                    costs[target] = costs[parent] + cost
                    parents.append(target)

    return sum(1 for c in costs if c <= K)