function solution(storey) {
    let x =[...String(storey)];
    let answer = 0;
    
    for (let i = 0; i < x.length; i++) {
        let arrP = +x[i];
        let arrP2 = +x[i+1];
        if (arrP < 5) answer += arrP;
        else if (arrP >= 5 && arrP2 >= 5) {
            answer += (10 - arrP);
            x[i+1] = arrP2+1;
        } else if (arrP >= 6) answer += (11 - arrP);
        else answer += arrP;
    }
    
    return answer;
}