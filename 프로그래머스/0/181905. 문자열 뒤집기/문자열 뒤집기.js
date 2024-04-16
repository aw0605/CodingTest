function solution(my_string, s, e) {
    let result = my_string.slice(s,e+1).split("").reverse().join("")
    let answer = my_string.replace(my_string.slice(s,e+1), result)
    return answer;
}