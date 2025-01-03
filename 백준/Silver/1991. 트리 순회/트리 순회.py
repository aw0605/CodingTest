import sys
input = sys.stdin.readline
 
n = int(input())
tree = {}
for n in range(n):
    root, l, r = input().strip().split()
    tree[root] = [l, r]
 
def pre(root):
    if root != ".":
        print(root, end='')
        pre(tree[root][0])
        pre(tree[root][1])
 
def inorder(root):
    if root != ".":
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])
 
def post(root):
    if root != ".":
        post(tree[root][0])
        post(tree[root][1])
        print(root, end='')

pre("A")
print()
inorder("A")
print()
post("A")