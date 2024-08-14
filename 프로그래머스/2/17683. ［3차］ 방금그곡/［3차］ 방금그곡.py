def change(s):
    s = s.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a').replace('B#', 'b')
    return s

def solution(m, musicinfos):
    answer = [0, '(None)']
    m = change(m)
    
    for info in musicinfos:
        t1, t2, title, notes = info.split(',')
        time = (int(t2[:2])-int(t1[:2]))*60 + int(t2[-2:])-int(t1[-2:])
        notes = change(notes)
        full_notes = notes * (time // len(notes)) + notes[:time % len(notes)]
        
        if m in full_notes and time > answer[0]: answer = [time, title]
    
    return answer[1]