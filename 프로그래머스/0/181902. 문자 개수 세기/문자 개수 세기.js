function solution(my_string) {
    let answer = Array(52).fill(0);
    let all_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for (let i = 0; i <= my_string.length; i++){
        let index = all_alpha.indexOf(my_string[i])
        if (index !== -1) answer[index]++;
    }
    return answer;
}