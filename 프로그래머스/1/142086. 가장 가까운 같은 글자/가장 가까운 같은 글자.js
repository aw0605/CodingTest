function solution(s) {
    let answer = [];
    let seen = {};
    for (let i = 0; i < s.length; i++) {
        let result = -1;
        if (s[i] in seen) {
            result = i - seen[s[i]];
        }
        seen[s[i]] = i;
        answer.push(result);
    }
    return answer;
}
