function solution(storey) {
    let answer = 0
    const x = String(storey).split("").map(a => Number(a))

    for(let i = x.length-1; i >= 0; i--) {
        if (x[i] > 5) {
            answer += 10 - x[i]
            if (i === 0) answer++
            x[i-1]++
        } else if(x[i] === 5 && i > 0 && x[i-1] >= 5) {
            answer+= 5
            x[i-1]++    
        } else answer += x[i]
    }
    
    return answer
}