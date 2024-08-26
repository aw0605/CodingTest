from itertools import accumulate

def collatz(k):
    arr = [k]
    while k != 1:
        k = k / 2 if k % 2 == 0 else k * 3 + 1
        arr.append(k)
        
    return arr

def solution(k, ranges):
    answer = []
    ubak = collatz(k)
    area = []
    
    for i in range(len(ubak) - 1): area.append((ubak[i] + ubak[i+1])/2)
    
    area = [0] + list(accumulate(area))
    n = len(area) - 1

    for a,b in ranges:
        k = n + b
        if a > k: answer.append(-1)
        elif a == k: answer.append(0)
        else: answer.append(area[k] - area[a])
        
    return answer
