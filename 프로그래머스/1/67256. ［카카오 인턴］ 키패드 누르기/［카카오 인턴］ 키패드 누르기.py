def solution(numbers, hand):
    answer = ''
    key = {
        1: (3,0), 2: (3,1), 3: (3,2),
        4: (2,0), 5: (2,1), 6: (2,2),
        7: (1,0), 8: (1,1), 9: (1,2),
        "*": (0,0), 0: (0,1), "#": (0,2)
    }
    sLeft = key["*"]
    sRight = key["#"]
    
    for n in numbers:
        curN = key[n]
        if n in [1,4,7]: 
            answer += "L"
            sLeft = curN
        elif n in [3,6,9]: 
            answer += "R"
            sRight = curN
        else: 
            lDist = abs(curN[0] - sLeft[0]) + abs(curN[1] - sLeft[1])
            rDist = abs(curN[0] - sRight[0]) + abs(curN[1] - sRight[1])
            if lDist > rDist:
                answer += "R"
                sRight = curN
            elif lDist < rDist:
                answer += "L"
                sLeft = curN
            else:
                if hand == "left":
                    answer += "L"
                    sLeft = curN
                else:
                    answer += "R"
                    sRight = curN
        
    return answer