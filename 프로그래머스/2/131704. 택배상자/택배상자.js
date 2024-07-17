function solution(order) {
    let answer = 0;
    let storage = []
    let j = 0;
    
    for (let i = 1; i <= order.length; i++){
        storage.push(i)
        while (storage.length && storage[storage.length-1] == order[j]){
            answer++
            j++
            storage.pop()
        }
    }
    return answer;
}