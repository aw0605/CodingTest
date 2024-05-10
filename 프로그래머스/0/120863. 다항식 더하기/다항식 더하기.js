function solution(polynomial) {
    let xnum = 0;
    let cnum = 0;
    for(v of polynomial.split(' + ')){
        if (!isNaN(v)) cnum += +v
        else v === "x"? xnum++ : xnum += +v.slice(0, v.length - 1)
    }
    
    if (xnum === 0) {return cnum.toString()}
    else if (xnum === 1) {
        return cnum !== 0? `x + ${cnum}` : "x"
    } else return cnum !== 0? `${xnum}x + ${cnum}` : `${xnum}x`
}