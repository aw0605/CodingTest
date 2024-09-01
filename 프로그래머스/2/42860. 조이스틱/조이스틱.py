def solution(name):
    cursor_num = len(name) - 1  
    spell_num = 0
    
    for i, s in enumerate(name):
        spell_num += min(ord(s) - ord('A'), ord('Z') - ord(s) + 1)

        next = i + 1
        while next < len(name) and name[next] == 'A': next += 1

        cursor_num = min([cursor_num, 2 * i + len(name) - next, i + 2 * (len(name) - next)])
            
    return spell_num + cursor_num