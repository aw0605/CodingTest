function solution(n, t, m, p) {
    let answer = ''
    let num = 0
    let str = ''
    
    while (answer.length < t) {
        if (str.length >= m) {
            answer += str[p - 1]
            str = str.slice(m)
        }
        else {
            str += num.toString(n).toUpperCase()
            num++
        }
    }
    
    return answer
}