def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    def dfs(node, p):
        cnt = 1
        for c in graph[node]:
            if c != p: cnt += dfs(c, node)
        return cnt
    
    min_diff = float("inf")
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        cnt_a = dfs(a,b)
        cnt_b = n - cnt_a
        
        min_diff = min(min_diff, abs(cnt_a - cnt_b))
        
        graph[a].append(b)
        graph[b].append(a)
        
    return min_diff