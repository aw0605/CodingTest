def solution(skill, skill_trees):
    answer = 0

    for v in skill_trees:
        skillArr = list(skill)

        for s in v:
            if s in skill:
                if s != skillArr.pop(0): break
        else: answer += 1

    return answer