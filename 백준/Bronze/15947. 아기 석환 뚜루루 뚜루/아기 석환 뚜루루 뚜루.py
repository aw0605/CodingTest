n = int(input())

arr = ["baby", "sukhwan", "tururu", "turu", "very", "cute", "tururu", 
      "turu", "in", "bed", "tururu", "turu", "baby", "sukhwan"]

cnt = n % 14 - 1
if "turu" not in arr[cnt]: print(arr[cnt])
else:
    res = arr[cnt] + "ru" * (n//14)
    ruN = res.count("ru")
    print(f"tu+ru*{ruN}" if ruN >= 5 else res)