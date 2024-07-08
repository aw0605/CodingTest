function solution(msg) {
    let answer = [];
    let dict = {}
    const alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for (let i = 0; i < 26; i++) dict[alpha[i]] = i+1
    
    let nextIndex = 27;
    let i = 0;
    
    while (i < msg.length) {
        let w = msg[i];
        let j = i + 1;
        
        // dict에 있는 wc 중 가장 긴 문자열 찾기
        while (j <= msg.length && dict[msg.slice(i, j)]) {
            w = msg.slice(i, j);
            j++;
        }
        // wc가 있다면 slice한 w의, 없다면 idx의 w의 value를 answer에 추가
        answer.push(dict[w]);
        // wc가 없다면 dict 업데이트
        if (j <= msg.length) dict[msg.slice(i, j)] = nextIndex++;
        // 다음에 찾을 문자로 이동
        i += w.length;
    }
    
    return answer;
}