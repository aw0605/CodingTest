def split_file(files):    
    route = 0
    answer = ['', '']
    for i, v in enumerate(files):
        if (route == 0):
            if (v.isnumeric() == True):
                answer[0] = files[:i].lower()
                route = 1
                answer[1] += v
        elif (route == 1):
            if (v.isnumeric() == True): answer[1] += v
            else: break
    answer[1] = int(answer[1])
    return answer


def solution(files):
    return sorted(files, key = lambda x:split_file(x))