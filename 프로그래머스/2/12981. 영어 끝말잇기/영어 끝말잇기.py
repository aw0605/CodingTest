def solution(n, words):
    answers = [words[0]]
    
    for i in range(1, len(words)):
        if (words[i] in answers) or (words[i-1][-1] != words[i][0]):
            return [(i%n)+1, (i//n)+1]
        answers.append(words[i])

    return [0,0]