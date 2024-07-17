function solution(order) {
    let storage = [], n = 1, answer = 0
    
    for (let i = 0; i < order.length; i++){
        let o = order[i]
        if (storage.length && storage[storage.length-1] == o){
            storage.pop()
            answer++
            continue
        }
        
        while (o != n){
            storage.push(n)
            n++
            if (n > order.length) return answer
        }
        n++
        answer++
    }
    
    return answer
}