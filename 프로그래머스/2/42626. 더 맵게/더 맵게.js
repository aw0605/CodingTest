function solution(scoville, K) {
    scoville.sort((a,b)=> b - a) 
    let answer = 0;
    let under_K = []
    let flag = 0

    for (let i = 0; i < scoville.length; ++i) {
        if (scoville[i] < K) under_K.push(scoville[i])
        else flag = 1
    }    

    let mixed = []
    let m_i = 0
    let i = 0
    let n1 = 0 
    let n2 = 0
    while (1){
        if (mixed[m_i] != undefined) {
            if (under_K.length != 0) {
                if (under_K.at(-1) < mixed[m_i]) n1 = under_K.pop()
                else {
                    n1 = mixed[m_i]
                    m_i++
                }
            }
            else {
                n1 = mixed[m_i]
                m_i++
            }
        }
        else {
            if (under_K.length != 0) n1 = under_K.pop()
            else break;
        }
        if (mixed[m_i] != undefined) {
            if (under_K.length != 0) {
                if (under_K.at(-1) < mixed[m_i]) n2 = under_K.pop()
                else {
                    n2 = mixed[m_i]
                    m_i++
                }
            }
            else {
                n2 = mixed[m_i]
                m_i++
            }
        }
        else {
            if (under_K.length != 0) n2 = under_K.pop()
            else {
                answer++
                break;
            }
        }

        if (n1+n2*2 < K) mixed.push(n1+n2*2)
        else flag = 1 
        answer++
    }

    return flag == 1 ? answer : -1
}
