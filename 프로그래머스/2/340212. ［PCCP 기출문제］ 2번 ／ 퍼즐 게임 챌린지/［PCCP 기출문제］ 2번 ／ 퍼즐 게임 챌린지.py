def solution(diffs, times, limit):
    left, right = 1, max(diffs)
    answer = right
    
    def solveTime(level):
        total = 0
        prev = times[0]
        
        for i in range(len(diffs)):
            diff = diffs[i]
            cur = times[i]
            
            if diff <= level: total += cur
            else:
                mistakes = diff - level
                total += (mistakes * (cur + prev)) + cur
            prev = cur
        
        return total
    
    while left <= right:
        mid = (left + right) // 2
        if solveTime(mid) <= limit:
            answer = mid
            right = mid - 1
        else: left = mid + 1
    
    return answer
