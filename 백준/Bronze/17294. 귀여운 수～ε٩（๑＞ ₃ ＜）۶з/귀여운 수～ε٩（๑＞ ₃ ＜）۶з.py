arr = list(map(int, input().strip()))

if len(arr) <= 2: 
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
    exit()
else:
    diff = arr[0] - arr[1]
    for i in range(1,len(arr)-1):
        cur = arr[i] - arr[i+1]
        if cur != diff:
            print("흥칫뿡!! <(￣ ﹌ ￣)>")
            exit()
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")