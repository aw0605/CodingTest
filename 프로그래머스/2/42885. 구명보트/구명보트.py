def solution(people, limit):
    boat = 0 
    people.sort()  
    first = 0
    last = len(people) - 1  
    
    while first <= last:
        if people[first] + people[last] <= limit: first += 1  
        last -= 1  
        boat += 1  
    
    return boat