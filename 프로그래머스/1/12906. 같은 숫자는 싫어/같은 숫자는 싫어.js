function solution(arr)
{
    let answer = [];
    for (let v of arr){
        if (answer.length === 0 || answer[answer.length-1] != v) answer.push(v)
    }
    
    return answer;
}