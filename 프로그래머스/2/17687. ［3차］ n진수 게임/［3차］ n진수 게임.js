function solution(n, t, m, p) {
    let answer = "";
    let cnt = 0;
    let str = "";

    for (let i = 0; str.length < m * t; i++) {
        str += i.toString(n).toUpperCase();
    }

    while (answer.length < t) {
        const s = str.slice(cnt, cnt + m);
        answer += s[p-1];
        cnt += m;
    }
    
  return answer;
}