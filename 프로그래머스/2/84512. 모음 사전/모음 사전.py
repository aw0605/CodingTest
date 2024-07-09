from itertools import product

def solution(word):
    answer = 0
    words = ["A", "E", "I", "O", "U"]
    dictWords = []
    for i in range(1,6):
        dictWords.extend([''.join(v) for v in product(words, repeat=i)])
    
    return sorted(dictWords).index(word) + 1