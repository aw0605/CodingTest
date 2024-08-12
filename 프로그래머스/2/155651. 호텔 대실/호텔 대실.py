def solution(book_time):
    bookings = [(int(start[:2]) * 60 + int(start[3:]), 
                 int(end[:2]) * 60 + int(end[3:]) + 10) 
                for start, end in book_time]
    bookings.sort()
    
    rooms = []
    
    for start, end in bookings:
        room_found = False
        for i in range(len(rooms)):
            if rooms[i] <= start:
                rooms[i] = end
                room_found = True
                break
        
        if not room_found: rooms.append(end)
    
    return len(rooms)