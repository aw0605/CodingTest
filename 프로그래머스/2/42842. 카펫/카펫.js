function solution(brown, yellow) {
    for(let i = 0; i <= yellow ** 0.5; i++){
        if(yellow % i === 0 && yellow/i*2 + i*2 + 4 === brown){
            return [yellow/i+2, i+2]
        }
    }
}