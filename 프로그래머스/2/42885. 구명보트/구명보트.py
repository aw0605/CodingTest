def solution(people, limit):
    people.sort()
    boat = 0
    i = 0
    j = len(people) - 1
    
    while i <= j:
        if people[i] + people[j] <= limit: i += 1
        j -= 1
        boat += 1
    
    return boat