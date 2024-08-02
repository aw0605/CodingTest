function solution(queue1, queue2) {
    let answer = 0
    const max = queue1.length * 2
    let sum = queue1.reduce((a,c,i)=> a + c - queue2[i],0)/2
    let [i,j] = [0,0]
    while (sum !== 0 && answer < max+3){
        if (sum > 0){
            const v = queue1[i]
            i++
            sum -= v
            queue2.push(v)
        } else {
            const v = queue2[j]
            j++
            sum += v
            queue1.push(v)
        }
        answer++
    }
    
    return sum !== 0 ? -1 : answer
}