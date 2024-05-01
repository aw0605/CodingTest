function solution(my_string, n) {
    var answer = '';
    for (let v of my_string) {
        answer += v.repeat(n)
    }
    return answer;
}