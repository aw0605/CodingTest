function solution(n, words) {
    let answers = [words[0]];
    
    for (let i = 1; i < words.length; i++){
        if (answers.includes(words[i]) || words[i-1][words[i-1].length-1] !== words[i][0]) return [(i%n)+1, Math.trunc(i/n)+1]
        answers.push(words[i])
    }

    return [0,0];
}