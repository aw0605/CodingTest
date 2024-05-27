import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    # 하나이상의 숫자 / SDT 중 하나 / *#없음 중 하나
    p = re.compile('(\d+)([SDT])([*#]?)')
    # 정규 표현식과 일치하는 부분 찾아 리스트로 반환 ["1","D",""]형태
    dart = p.findall(dartResult)
    
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0: dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    return sum(dart)