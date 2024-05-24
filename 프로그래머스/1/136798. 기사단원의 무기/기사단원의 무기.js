function solution(number, limit, power) {
    let gcdArr = [1];
    
    for (let k = 2; k <= number; k++){
        let gcdN = 0
        for (let i = 1; i <= k ** 0.5; i++){
            if (k % i == 0) {
                gcdN++
                if (i !== k / i) gcdN++;
            };
        }
        gcdArr.push(gcdN)
    }

    return gcdArr.reduce((a,c) => a + (c <= limit? c : power), 0);
}