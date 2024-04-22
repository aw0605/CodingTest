function solution(arr) {
    let answer = 0;
    while (true) {
        let arr_x = arr.map((v) => {
            if (v % 2 === 0 && v >= 50) return v / 2
            else if (v % 2 !== 0 && v < 50) return v * 2 + 1
            else return v
        })
        if (arr.every((v,i) => v == arr_x[i])) return answer
        else {
            answer++
            arr = arr_x
        }
    }
    return answer;
}