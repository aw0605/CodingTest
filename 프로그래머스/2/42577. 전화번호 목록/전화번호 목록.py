def solution(phone_book):
    phoneBook = sorted(phone_book)

    for p, v in zip(phoneBook, phoneBook[1:]):
        if v.startswith(p): return False
        
    return True