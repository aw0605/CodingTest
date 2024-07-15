def solution(skill, skill_trees):
    answer = 0
    
    for v in skill_trees:
        order = ""
        for s in v:       
            if s in skill: order += s
        
        if skill[:len(order)] == order: answer += 1
    
    return answer