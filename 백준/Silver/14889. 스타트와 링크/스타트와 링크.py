import sys
input = sys.stdin.readline

n = int(input())
status = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
diff = sys.maxsize

def dfs(a,idx):
    global diff
    if a == n//2:
        start = 0
        link = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]: start += status[i][j]
                elif not visited[i] and not visited[j]: link += status[i][j]
        diff = min(diff, abs(start - link))
        return
    else:
        for i in range(idx,n):
            if not visited[i]:
                visited[i] = True
                dfs(a+1, i+1)
                visited[i] = False
                
dfs(0,0)
print(diff)
    