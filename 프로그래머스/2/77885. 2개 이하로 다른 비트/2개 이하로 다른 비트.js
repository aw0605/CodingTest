function solution(numbers) {
    return numbers.map(v => {
        let n = '0'+v.toString(2);
        if (n[n.length - 1] === '0') {
            n = n.slice(0, n.length-1) + '1';
        } else {
            const i = n.lastIndexOf('01');
            n = n.slice(0,i) + '10' + n.slice(i+2, n.length);
        }
        
        return parseInt(n, 2);
    })
}