def solution(picks, minerals):
    answer = 0
    m_score = []
    m_groups = []
    
    for i in minerals[:5*sum(picks)]:
        if i == "diamond": m_score.append(25)
        elif i == "iron": m_score.append(5)
        else: m_score.append(1)

    for i in range(len(m_score)//5+1): m_groups.append(m_score[5*i:5*(i+1)])

    m_groups.sort(key= lambda x: sum(x), reverse=True)

    for i in range(len(picks)) :
        while (picks[i] != 0 and len(m_groups) != 0):
            if i == 0: answer += len(m_groups[0])
            elif i == 1:
                for j in m_groups[0]:
                    if j == 1: answer += 1
                    else: answer += j//5
            else: answer += sum(m_groups[0])
            
            picks[i] -= 1
            del m_groups[0]

    return answer