import sys
input = sys.stdin.readline

n,m = map(int, input().split())
name_dic = {}
id_dic = {}

for i in range(1, n+1):
    cur = input().strip()
    name_dic[cur] = i
    id_dic[i] = cur
    
for _ in range(m):
    quiz = input().strip()
    if quiz.isdigit(): print(id_dic[int(quiz)])
    else: print(name_dic[quiz])
