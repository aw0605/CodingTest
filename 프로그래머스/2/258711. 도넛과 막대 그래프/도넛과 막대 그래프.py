from collections import defaultdict

def find_centroid(graph, inDegree, outDegree):
    for node in graph.keys():
        if inDegree[node] == 0 and outDegree[node] >= 2: return node

def count_graphs(centroid, graph, inDegree, outDegree):
    count = [0, 0, 0]
    visited = set()
    
    for start in graph[centroid]:
        visited.add(start)
        curr = start
        while curr:
            if outDegree[curr] == 0:
                count[1] += 1
                break
            elif outDegree[curr] == 2:
                count[2] += 1
                break
            curr = graph[curr][0]
            if curr in visited and outDegree[curr] == 1:
                count[0] += 1
                break
            visited.add(curr)
    return [centroid] + count

def solution(edges):
    graph = defaultdict(list)
    inDegree = defaultdict(int)
    outDegree = defaultdict(int)
    for start, end in edges:
        graph[start].append(end)
        inDegree[end] += 1
        outDegree[start] += 1

    centroid = find_centroid(graph, inDegree, outDegree)
    return count_graphs(centroid, graph, inDegree, outDegree)