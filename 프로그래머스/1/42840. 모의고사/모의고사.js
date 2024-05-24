function solution(answers) {
    let answer = []
    const a1 = [1,2,3,4,5]
    const a2 = [2,1,2,3,2,4,2,5]
    const a3 = [3,3,1,1,2,2,4,4,5,5]
    const cA = [0,0,0]
    for (let i = 0; i < answers.length; i++){
        if (a1[i % 5] === answers[i]) cA[0]++
        if (a2[i % 8] === answers[i]) cA[1]++
        if (a3[i % 10] === answers[i]) cA[2]++
    }
    for (let j = 0; j < 3; j++){
        if (cA[j] === Math.max(...cA)) answer.push(j+1)
    }
    return answer;
}