function solution(cards) {
    let answer = [];
    
    for (let i = 0; i < cards.length; i++) {
        let group = 0;
        while (cards[i] !== 0) {
            let ni = cards[i] - 1;
            cards[i] = 0;
            i = ni;
            group++;
        }
        answer.push(group);
    }
    
    answer.sort((a, b) => b - a);
    
    return answer[0] * answer[1];
}
