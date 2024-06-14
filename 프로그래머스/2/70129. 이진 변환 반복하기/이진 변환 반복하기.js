function solution(s) {
    let answer = [0,0]
    
    while (s != "1"){
        answer[1] += [...s].filter(v => v == "0").length
        s = ((s.replaceAll("0", "")).length).toString(2);
        answer[0]++;
    }
    
    return answer
}