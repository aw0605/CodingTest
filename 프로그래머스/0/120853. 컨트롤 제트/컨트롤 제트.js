function solution(s) {
    let sArr = s.split(" ")
    let nArr = []
    for (let v of sArr){
        if (v === "Z") nArr.pop()
        else nArr.push(v)
    }
    return nArr.reduce((a,c) => +a + +c, 0);
}