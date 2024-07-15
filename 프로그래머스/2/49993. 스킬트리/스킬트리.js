function solution(skill, skill_trees) {
    let answer = 0;
    
    for (let v of skill_trees){
        let order = ""
        for (let s of v){
            if (skill.includes(s)) order += s
        }
        
        if (skill.slice(0, order.length) === order) answer++
    }
    
    return answer;
}