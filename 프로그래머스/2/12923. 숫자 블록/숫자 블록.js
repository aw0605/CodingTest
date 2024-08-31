function check(num) {       
    let checkArr = [];        
    if (num === 1) return 0;

    for (let i = 2; i <= Math.sqrt(num); i++){
        if (num % i === 0) {
            checkArr.push(i);
            if (num/i <= 10**7) return num/i;
        }
    }
    if (checkArr.length !== 0) return checkArr[checkArr.length-1];
    return 1;
}

function solution(begin, end) {
    let answer = [];
    
    for (let i = begin; i <= end; i++){
        let checkNum = check(i)
        if (checkNum !== undefined) answer.push(checkNum)
    }
    
    return answer;
}