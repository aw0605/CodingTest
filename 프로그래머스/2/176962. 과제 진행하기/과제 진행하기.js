function solution(plans) {
    let answer = [];
    let hash  ={}
    
    plans.forEach(el=>{
        el[1] = convertTime(el[1])
        el[2] = Number(el[2])
        hash[el[1]] = [el[2],el[0]]
    })

    plans.sort((a,b)=>a[1]-b[1])

    let startTime = plans[0][1]
    let stack =[]
    let finish = 0
    
    while (finish < plans.length){
        if (hash[startTime]) stack.push(hash[startTime])
        if(stack.length){
            stack[stack.length-1][0]--
            if (stack[stack.length-1][0] === 0) {
                answer.push(stack[stack.length-1][1])
                stack.pop()
                finish++
            }
        }
        startTime++
    }

    function convertTime(time){
        let [h,m] = time.split(':').map(Number)
        return h*60+m
    }

    return answer;
}