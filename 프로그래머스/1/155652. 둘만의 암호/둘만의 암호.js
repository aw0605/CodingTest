function solution(s, skip, index) {
    const alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'].filter(v => !skip.includes(v));

    return [...s].reduce((a,c) => a += alpha[(alpha.indexOf(c)+index)%alpha.length], "");
}