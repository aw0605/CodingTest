from collections import deque

def solution(info, edges):
    answer = 0
    q = deque([(0,1,0,set())])
    
    def build_tree(info, edges):
        tree = [[] for _ in range(len(info))]
        for edge in edges: tree[edge[0]].append(edge[1])
        return tree
    tree = build_tree(info, edges)
    
    while q:
        cur, sheep, wolf, visited = q.popleft()
        answer = max(answer, sheep)
        visited.update(tree[cur])
        for nNode in visited:
            if info[nNode]:
                if sheep != wolf + 1:
                    q.append((nNode,sheep,wolf+1,visited-{nNode}))
            else:
                q.append((nNode,sheep+1,wolf,visited-{nNode}))
        
    return answer