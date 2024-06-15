function solution(brown, yellow) {
    for (let i = 1; i <= yellow**0.5; i++){
        if (yellow % i == 0){
            let w = (yellow / i) + 2
            let h = i + 2
            
            if (brown == ((w + h - 2) * 2)) return [w, h]
        }
    }
}