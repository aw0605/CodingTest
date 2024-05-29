function solution(s, skip, index) {
    let answer = '';
    const atoz = 'abcdefghijklmnopqrstuvwxyz'.match(
        new RegExp(`[^${skip}]`, 'g'),
    );
    for (const w of s) {
        const newIdx = atoz.indexOf(w) + index;
        answer += atoz[newIdx % atoz.length];
    }
  return answer;
}