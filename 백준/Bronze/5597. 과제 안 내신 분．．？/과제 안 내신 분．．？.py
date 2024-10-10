import sys

arr = [i+1 for i in range(30)]

for _ in range(28):
    submit = int(sys.stdin.readline())
    arr.remove(submit)

print(min(arr))
print(max(arr))