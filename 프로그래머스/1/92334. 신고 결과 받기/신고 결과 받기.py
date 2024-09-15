def solution(id_list, report, k):
    answer = []
    reported_user = {}
    count = {}
    
    for r in report:
        reporter, reported = r.split( )
        if reported not in reported_user: reported_user[reported] = set()
        reported_user[reported].add(reporter)
        
    for reported, reporters in reported_user.items():
        if len(reporters) >= k:
            for uid in reporters:
                if uid not in count: count[uid] = 1
                else: count[uid] += 1
                
    for i in range(len(id_list)):
        if id_list[i] not in count: answer.append(0)
        else: answer.append(count[id_list[i]])
        
    return answer