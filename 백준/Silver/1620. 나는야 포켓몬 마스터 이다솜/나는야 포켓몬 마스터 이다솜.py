import sys
input = sys.stdin.readline

n,m = map(int, input().split())
name_dic = {}
id_dic = {}

for i in range(1, n+1):
    cur = input().strip()
    name_dic[cur] = i
    id_dic[i] = cur

ans = []
for _ in range(m):
    quiz = input().strip()
    if quiz.isdigit(): ans.append(id_dic[int(quiz)])
    else: ans.append(str(name_dic[quiz]))

print('\n'.join(ans))
