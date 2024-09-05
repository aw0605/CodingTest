from collections import defaultdict, deque

def solution(edges):
    answer = [0, 0, 0, 0]
    start, donut, bar, eight = 0, 1, 2, 3
    graph = defaultdict(list)
    degrees = defaultdict(lambda: [0, 0])

    for edge in edges:
        a, b = edge
        graph[a].append(b)

    for node, nodes in graph.items():
        for adjacent in nodes:
            degrees[node][0] += 1
            degrees[adjacent][1] += 1

    for node, degree in degrees.items():
        outd, ind = degree

        if outd == 0: answer[bar] += 1
        elif outd == 2:
            if ind > 0: answer[eight] += 1
            else:
                answer[start] = node
                root = node
        elif outd > 2:
            answer[start] = node
            root = node

    answer[donut] = degrees[root][0] - answer[bar] - answer[eight]

    return answer