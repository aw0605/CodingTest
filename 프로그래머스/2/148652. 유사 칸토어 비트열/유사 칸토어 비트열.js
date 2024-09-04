function solution(n, l, r) {
    let answer = r - l + 1;
    
    for (let num = l - 1; num < r; num++) {
        let current = num;
        while (current >= 1) {
            let a = Math.floor(current / 5), b = current % 5;
            if (b === 2 || a === 2) {
                answer--;
                break;
            }
            current = a;
        }
    }

    return answer;
}
