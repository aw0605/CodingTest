function solution(n, m) {
    let r;  //나머지 저장 변수
    let nm = n * m;
    for (r = n % m; r !== 0; n = m, m = r, r = n % m) {}  
    // 유클리드 호제법으로 최대공약수 계산
    // 두수 n,m의 최대공약수 = m과 n % m의 최대 공약수
    return [m, nm / m];
}