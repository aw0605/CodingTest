function isPrime(num) {
    if (num < 2) return false;
    if (num === 2) return true;
    for (var i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }
    return true;
}

function solution(numbers) {
    let answer = 0;

    let n = numbers.split('');
    let nums = new Set()

    function combi(a, s) {
        if (s.length > 0) {
            if (nums.has(+s) === false) {
                nums.add(+s);
                if (isPrime(+s)) answer++;
            }
        }
        if (a.length > 0) {
            for (let i = 0; i< a.length; i++) {
                let t = a.slice(0)
                t.splice(i,1);
                combi(t,s + a[i]);
            }
        }
    }
    
    combi(n,'');

    return answer;
}