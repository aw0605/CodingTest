def GCD(x, y):
    while y: 
        x,y = y, x % y
    return x
 
def notDiv(arr, gcd):
    for n in arr:
        if n % gcd == 0: return False
    return True

def solution(arrayA, arrayB):
    answer = 0
    gcdA = arrayA[0]
    gcdB = arrayB[0]
    
    for a in arrayA[1:]: gcdA = GCD(a, gcdA)
    for b in arrayB[1:]:gcdB = GCD(b, gcdB)
        
    if notDiv(arrayA, gcdB): answer = max(answer, gcdB)
    if notDiv(arrayB, gcdA):answer = max(answer, gcdA)
        
    return answer