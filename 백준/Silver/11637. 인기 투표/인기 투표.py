import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    maxV = max(arr)
    if arr.count(maxV)>1:
        print('no winner')
    else:
        print(f"{['minority','majority'][maxV > sum(arr)//2]} winner {arr.index(maxV)+1}")