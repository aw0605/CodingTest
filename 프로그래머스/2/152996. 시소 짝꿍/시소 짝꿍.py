def solution(weights):
    answer = 0
    dic = {}
    friend_list = [2,3/2,4/3]
    
    for weight in weights:
        if weight in dic: dic[weight] += 1
        else: dic[weight] = 1

    for weight in dic:
        if dic[weight]>1:
            answer += dic[weight] * (dic[weight]-1)/2
        for friend in friend_list:
            if weight * friend in dic:
                answer += dic[weight] * dic[weight*friend]

    return answer