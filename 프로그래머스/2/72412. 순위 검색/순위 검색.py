from itertools import combinations
from collections import defaultdict
import bisect

def solution(info, query):
    answer = []

    def combi(arr, select_num): return list(combinations(arr, select_num))

    info_score = defaultdict(list)
    info_score[""] = []

    for v in info:
        val = v.split(" ")
        score = int(val.pop())
        info_score[""].append(score)

        for i in range(1, 5):
            comb = combi("0123", i)
            for c in comb:
                key = ''.join([val[int(index)] for index in c])
                info_score[key].append(score)

    for key in info_score: info_score[key].sort()

    for v in query:
        v = v.replace(" and ", "").replace("-", "").split(" ")
        key = v[0]
        score = int(v[1])

        if key in info_score:
            scores = info_score[key]
            index = bisect.bisect_left(scores, score)
            answer.append(len(scores) - index)
        else: answer.append(0)

    return answer
