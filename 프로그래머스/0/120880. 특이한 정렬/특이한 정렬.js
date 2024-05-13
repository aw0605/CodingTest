function solution(numlist, n) {
    return numlist.sort(function(a,b){
        if (Math.abs(n-a) < Math.abs(n-b)) return -1
        if (Math.abs(n-a) > Math.abs(n-b)) return 1
        return b - a
    });
}