import sys

setArr = set()

for _ in range(10):
    n = int(sys.stdin.readline())
    setArr.add(n % 42)
    
print(len(setArr))