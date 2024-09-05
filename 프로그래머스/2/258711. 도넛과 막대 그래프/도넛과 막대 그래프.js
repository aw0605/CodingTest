function solution(edges) {    
    const graphInfo = {}

    edges.forEach(([send,receive])=>{
        graphInfo[send] ||= { sendCount:0, receiveCount:0 }
        graphInfo[receive] ||= { sendCount:0, receiveCount:0 }

        graphInfo[send].sendCount++
        graphInfo[receive].receiveCount++
    })

    let s = 0
    let count = 0
    let bar = 0, donut = 0, eight = 0

    for (let v in graphInfo){
        const { sendCount, receiveCount } = graphInfo[v]
        if (sendCount >= 2 && receiveCount === 0){
            s = +v
            count = sendCount
        }
        if (sendCount == 0) bar++
        if (sendCount >= 2 && receiveCount >= 2) eight++
    }

    donut = count - eight - bar

    return [s, donut, bar, eight];
}