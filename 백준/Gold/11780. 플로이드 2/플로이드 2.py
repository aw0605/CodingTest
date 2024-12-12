import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * n for _ in range(n)]
path = [[-1] * n for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    a -= 1 
    b -= 1
    graph[a][b] = min(graph[a][b], c)
    path[a][b] = a
    
def floyd():
    for k in range(n):
        graph[k][k] = 0
        path[k][k] = -1
        for i in range(n):
            for j in range(n):
                d = graph[i][k] + graph[k][j]
                if graph[i][j] > d:
                    graph[i][j] = d
                    path[i][j] = path[k][j]

floyd()
            
for row in graph:
    for i in row:
        print(i if i != INF else 0, end=" ")
    print()

for i in range(n):
    for j in range(n):
        if path[i][j] == -1:
            print(0)
            continue
        ans = []
        while True:
            if j == i: break
            ans.append(j+1)
            j = path[i][j]
        print(len(ans)+1, i+1, *ans[::-1])