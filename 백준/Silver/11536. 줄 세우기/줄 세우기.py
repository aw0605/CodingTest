import sys
input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]
sortArr = sorted(arr)
reverseArr = sorted(arr, reverse=True)

if arr == sortArr: print("INCREASING")
elif arr == reverseArr: print("DECREASING")
else: print("NEITHER")