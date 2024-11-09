from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
status = [list(map(int, input().split())) for _ in range(n)]

people = range(n)
diff = float('inf')

def team_stat(team):
    stat = 0
    for i, j in combinations(team, 2):
        stat += status[i][j] + status[j][i]
    return stat

for start in combinations(people, n // 2):
    link = [i for i in people if i not in start]

    start_st = team_stat(start)
    link_st = team_stat(link)

    diff = min(diff, abs(start_st - link_st))

print(diff)