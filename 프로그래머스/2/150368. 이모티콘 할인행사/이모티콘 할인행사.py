from itertools import product

def permutation(arr, select_num):
    if select_num == 1: return [[v] for v in arr]
    
    result = []
    for v in arr:
        fixed = v
        rest_arr = arr
        permutation_arr = permutation(rest_arr, select_num - 1)
        combine_fix = [[fixed] + p for p in permutation_arr]
        result.extend(combine_fix)
    
    return result

def solution(users, emoticons):
    answer = []
    permutations = list(product([10, 20, 30, 40], repeat=len(emoticons)))

    for combi in permutations:
        service = 0
        costs = [0] * len(users)

        for ci, c in enumerate(combi):
            for ui, user in enumerate(users):
                if user[0] <= c:
                    costs[ui] += emoticons[ci] * (100 - c) / 100

        total_sum = 0
        for i in range(len(costs)):
            if costs[i] < users[i][1]: total_sum += costs[i]
            else: service += 1
        
        answer.append([service, total_sum])

    return sorted(answer, key=lambda x: (-x[0], -x[1]))[0]
