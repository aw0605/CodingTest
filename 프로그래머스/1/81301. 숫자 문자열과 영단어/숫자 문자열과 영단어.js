function solution(s) {
    const enNum = ['zero', 'one', 'two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];

    for(let v of enNum){               
        if(s.includes(v)) s = s.replaceAll(v, enNum.indexOf(v));
    }

    return Number(s);
}