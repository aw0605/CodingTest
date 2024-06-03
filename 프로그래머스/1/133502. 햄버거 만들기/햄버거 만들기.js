function solution(ingredient) {
    let answer = 0;
    let burger = []
    
    for (let v of ingredient){
        burger.push(v)
        if (
            burger[burger.length - 1] === 1 &&
            burger[burger.length - 2] === 3 &&
            burger[burger.length - 3] === 2 &&
            burger[burger.length - 4] === 1
        ) {
            answer++;
            burger.splice(-4);
        }
    }
    
    return answer;
}