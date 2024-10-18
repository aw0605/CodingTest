def divisors(n):
    divisors = []
    
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n//i: divisors.append(n//i)
    
    divisors.sort()
    
    return divisors[:-1]



while True :
    n = int(input())
    if n == -1: break
    arr = divisors(n)
    result = sum(arr)
    
    if n == result: print(n, "=", " + ".join(map(str,arr)))
    else : print(n, "is NOT perfect.")