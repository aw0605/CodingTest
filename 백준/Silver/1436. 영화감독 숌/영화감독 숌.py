import sys

input = sys.stdin.readline
print = sys.stdout.write

arr = [666]

def count_six(n):
  count = 0
  for i in reversed(str(n)):
    if i == '6':
      count += 1
    else :
      break
  return count

n = int(input())
count = 1
i = 1

while(count != n):
  six_count = count_six(i)
  if six_count:
    for j in range(10**six_count):
      arr.append(str(i) + "666"[:3-six_count] + str(j).zfill(six_count))
      count += 1
      if count == n: break
  else:
    arr.append(str(i) + "666")
    count += 1
  i += 1

print('%s' % arr[n-1])