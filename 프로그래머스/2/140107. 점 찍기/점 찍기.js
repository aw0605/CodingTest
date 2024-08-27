function solution(k, d) {
    let answer = 0;
    
    function maxY(x){
        return (Math.floor(Math.sqrt(d*d-x*x)));
    }
    
    for (var x = 0; x <= d; x+=k){
        answer += ((Math.floor(maxY(x)/k))+1);
    }
    
    return answer;
}