answer = []

def solution(k, dungeons):

    def dfs(k, dungeons, depth):
        temp = True
        for d in range(len(dungeons)):
            dun = dungeons[d]
            if dun[0] <= k and dun[1] <= k:
                temp_dungeons = dungeons[:]
                del temp_dungeons[d]
                dfs(k-dun[1], temp_dungeons, depth+1)
                temp = False
        if temp:
            global answer
            answer.append(depth)
    dfs(k, dungeons, 0)

    return max(answer)
