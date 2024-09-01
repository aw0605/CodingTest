function solution(name) {
    let cursorNum = name.length - 1;
    let spellNum = 0;
    
    for (let i = 0; i < name.length; i++) {
        const s = name[i];
        spellNum += Math.min(s.charCodeAt(0) - 'A'.charCodeAt(0), 'Z'.charCodeAt(0) - s.charCodeAt(0) + 1);

        let next = i + 1;
        while (next < name.length && name[next] === 'A') next++;

        cursorNum = Math.min(cursorNum, 2 * i + name.length - next, i + 2 * (name.length - next));
    }
    
    return spellNum + cursorNum;
}
