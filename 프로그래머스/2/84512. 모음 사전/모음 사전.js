function solution(word) {
    return word.split('')
            .reduce((a,c,i) => a + ((5**(5-i)-1) / 4) * ('AEIOU'.indexOf(c)) + 1, 0)
}