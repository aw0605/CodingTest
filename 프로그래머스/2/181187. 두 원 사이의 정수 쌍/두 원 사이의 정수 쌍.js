function solution(r1, r2) {
    let answer = 0;

    for (let i = 1; i < r2; i++) {
        let num2 = Math.floor(Math.sqrt(r2 * r2 - i * i));
        if (i >= r1) answer += 4 * (num2 + 1);
        else {
            let num1 = Math.floor(Math.sqrt(r1 * r1 - i * i));
            if (num1 * num1 + i * i === r1 * r1) answer += 4 * (num2 - num1 + 1);
            else answer += 4 * (num2 - num1);
        }
    }

    return answer + 4;
}
