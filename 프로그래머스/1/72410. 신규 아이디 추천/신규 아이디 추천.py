import re

def solution(new_id):
    new_id = re.sub('[^0-9a-z\-._]', '', new_id.lower())
    new_id = re.sub('\.{2,}', '.', new_id)
    new_id = re.sub('^[.]|[.]$', '', new_id)
    
    if new_id == "": new_id = "a"
    if len(new_id) >= 16:
        new_id = re.sub('[.]$', '', new_id[:15])
    if len(new_id) < 3: new_id += new_id[-1] * (3-len(new_id))
    
    return new_id