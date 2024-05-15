function solution(s){
    let p = 0;
    let y = 0;

    for(let v of s.toLowerCase()){
        if (v === "p") p++
        else if(v === "y") y++
    }
    
    return p === y
}