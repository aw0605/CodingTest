def change_time(time):
    time = time.split(":")
    return int(time[0]) * 60 + int(time[1])

def solution(plans):
    answer = []

    plans = [[name, change_time(start), int(playtime)] for name, start, playtime in plans]
    plans.sort(key=lambda x: x[1], reverse=True)

    while plans:
        name, start, playtime = plans.pop()

        for i in range(len(answer)):
            if start < answer[i][1]: answer[i][1] += playtime

        answer.append([name, start + playtime])

    answer.sort(key=lambda x: x[1])
    
    return [v[0] for v in answer]
