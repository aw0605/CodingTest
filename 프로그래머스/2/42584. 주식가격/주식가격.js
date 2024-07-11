function solution(prices) {
    const answer = [];
    const tmp = prices.reverse()
    
    while (tmp.length) {
        const price = tmp.pop()
        let sec = 0;
        for (let i = tmp.length - 1; i >= 0; i--) {
            sec += 1
            if (price > tmp[i]) break
        }
        answer.push(sec)
    }
    
    return answer ;
}