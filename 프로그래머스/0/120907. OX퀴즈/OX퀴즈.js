function solution(quiz) {
    let answer = [];
    for (let v of quiz){
        let result;
        let [X,op,Y,S,Z] = v.split(" ");
        op === "+"? result = +X + +Y : result = +X - +Y
        result === +Z? answer.push("O") : answer.push("X")
    }
    return answer
}