def solution(record):
    answer = []
    user = {}
    
    for v in record:
        v = v.split()
        if v[0] in ["Enter", "Change"]: user[v[1]] = v[2]
    
    for v in record:
        v = v.split()
        if v[0] == "Enter": answer.append(f'{user[v[1]]}님이 들어왔습니다.')
        elif v[0] == "Leave": answer.append(f'{user[v[1]]}님이 나갔습니다.')
    
    return answer