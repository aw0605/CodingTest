import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

inorderIdx = {v: i for i, v in enumerate(inorder)}

def find_child(il, ir, pl, pr):
    if il > ir: return
    
    root = postorder[pr]
    print(root, end=" ")
    
    rootIdx = inorderIdx[root]
    offset = rootIdx - il
    
    find_child(il, rootIdx-1, pl, pl+offset-1)
    find_child(rootIdx+1, ir, pl+offset, pr-1)

find_child(0, n-1, 0, n-1)