function solution(participant, completion) {
    let answer = '';
    const pArr = participant.sort()
    const cArr = completion.sort()
    
    for (let i = 0; i < pArr.length; i++){
        if (pArr[i] !== cArr[i]) 
            return pArr[i]
    }
}