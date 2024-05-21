function solution(n, arr1, arr2) {
    let answer = new Array(n).fill("");

    for (let i = 0; i < n; i++){
        let a1V = arr1[i].toString(2).padStart(n, "0")
        let a2V = arr2[i].toString(2).padStart(n, "0")
        
        for (let j = 0; j < n; j++){
            (a1V[j] === "1" || a2V[j] === "1")? answer[i] += "#" : answer[i] += " "
        }

    }
    return answer;
}