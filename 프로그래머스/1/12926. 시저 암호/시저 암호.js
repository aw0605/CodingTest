function solution(s, n) {
    let answer = "";

    for (let v of s) {
        if (v === ' ') {
            answer += v;
        } else {
            let charCode = v.charCodeAt(0);
            if (v >= 'A' && v <= 'Z') {
                answer += String.fromCharCode((charCode-65+n)%26 + 65);
            } else {
                answer += String.fromCharCode((charCode-97+n)%26 + 97);

            }
        }
    }

    return answer;
}