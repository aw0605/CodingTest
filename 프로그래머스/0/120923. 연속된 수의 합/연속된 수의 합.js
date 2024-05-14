function solution(num, total) {
    var min = Math.ceil(total/num - Math.floor(num/2));

    return new Array(num).fill(0).map((_,i)=>{return i + min;});
}