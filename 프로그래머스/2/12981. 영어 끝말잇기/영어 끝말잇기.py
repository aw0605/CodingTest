def solution(n, words):
    words_set = set()
    prev_word = words[0][0]
    
    for i,w in enumerate(words):
        if w in words_set or w[0] != prev_word:
            return [(i%n)+1, (i//n)+1]
        words_set.add(w)
        prev_word = w[-1]

    return [0,0]