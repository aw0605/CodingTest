function solution(topping) {
    let answer = 0;
    const brother = {}
    const chulsu = new Set()
    
    let broKind = 0

    for (let v of topping) {
        if (brother[v]) brother[v]++
        else {
            brother[v] = 1;
            broKind++
        }
    }
    
    for (let v of topping) {
        chulsu.add(v)
        brother[v]--

        if (!brother[v]) broKind--
        if (chulsu.size === broKind) answer++
    }

    return answer;
}