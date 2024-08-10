def solution(n):
    answer = ''
    arr = [4,1,2]
    
    while n > 0:
        answer = str(arr[n%3]) + answer
        n = (n-1)//3
        
    return answer