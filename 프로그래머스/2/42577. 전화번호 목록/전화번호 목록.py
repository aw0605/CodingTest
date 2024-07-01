def solution(phone_book):
    setNumbers = set(phone_book)
    
    for v in phone_book:
        for i in range(1, len(v)):
            prefix = v[:i]
            if prefix in setNumbers: return False
        
    return True