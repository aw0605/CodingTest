function solution(s) {
    if(s.length % 2) return 0;

    let answer = 0;
    const pair = { "}":"{", "]":"[", ")":"("};

    for (let i = 0; i < s.length; i++) {
        const stack = [];
        const rotS = s.slice(i) + s.slice(0, i);

        for (let j of rotS) {
            if (stack.length && stack[stack.length-1] === pair[j]) stack.pop()
            else stack.push(j)
        }
        if (!stack.length) answer++;
    }

    return answer;
}