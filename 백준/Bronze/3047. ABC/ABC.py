import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
nums.sort()
s = input().strip()

ans = []
for v in s:
    if v == "A": ans.append(nums[0])
    elif v == "B": ans.append(nums[1])
    else: ans.append(nums[2])
        
print(" ".join(map(str, ans)))