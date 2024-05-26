function solution(babbling) {
    // 주어진 발음 1회 이상 연속 반복 확인
    const reg1 = /(aya|ye|woo|ma)\1+/;
    // 처음부터 끝까지 주어진 발음으로만 구성되어 있는지 확인 
    const reg2 = /^(aya|ye|woo|ma)+$/;

    // test: 주어진 정규식 만족하는지 boolean리턴
    return babbling.filter((v) => (!reg1.test(v) && reg2.test(v))).length;
}
