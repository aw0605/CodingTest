def solution(record):
    user = {v.split()[1]:v.split()[-1] for v in record if v.startswith('Enter') or v.startswith('Change')}
    
    return [f'{user[v.split()[1]]}님이 들어왔습니다.' if v.startswith('Enter') else f'{user[v.split()[1]]}님이 나갔습니다.' for v in record if not v.startswith('Change')]
