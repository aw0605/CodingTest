function solution(picture, k) {
    var answer = [];
    picture.map(v => {
        let repeat = [...v].map(v => v.repeat(k)).join("")
        for (let i = 0; i < k; i++){
            answer.push(repeat)
        }
    })
    return answer;
}