function solution(number, k) {
    const answer = []
    let i = 0

    answer.push(number[i++])
    
    while (answer.length < number.length - k || i < number.length) {
        if (k && answer[answer.length-1] < number[i]) {
            answer.pop()
            k--
            continue
        }
        answer.push(number[i++])
    }

    return answer.slice(0, number.length - k).join('')
}