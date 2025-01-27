arr = list(map(int, input().strip()))
cute = 1
for i in range(len(arr)-1):
    if arr[0] - arr[1] != arr[i] - arr[i+1]:
        cute = 0
        break

print(['흥칫뿡!! <(￣ ﹌ ￣)>','◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!'][cute])