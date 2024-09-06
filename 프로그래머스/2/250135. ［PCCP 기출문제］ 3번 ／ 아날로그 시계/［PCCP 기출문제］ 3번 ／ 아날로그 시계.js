function solution(h1, m1, s1, h2, m2, s2) {
    let answer = 0;
    let sTime = h1 * 3600 + m1 * 60 + s1;
    let eTime = h2 * 3600 + m2 * 60 + s2;

    if (sTime === 0 * 3600 || sTime === 12 * 3600) answer++

    while (sTime < eTime) {
        let hCurAngle = (sTime / 120) % 360;
        let mCurAngle = (sTime / 10) % 360;
        let sCurAngle = (sTime * 6) % 360;

        let hNextAngle = ((sTime+1)/120) % 360 === 0 ? 360 : ((sTime+1)/120) % 360;
        let mNextAngle = ((sTime+1)/10) % 360 === 0 ? 360 : ((sTime+1)/10) % 360;
        let sNextAngle = ((sTime+1)*6) % 360 === 0 ? 360 : ((sTime+1)*6) % 360;

        if (sCurAngle < hCurAngle && sNextAngle >= hNextAngle) answer++
        if (sCurAngle < mCurAngle && sNextAngle >= mNextAngle) answer++
        if (sNextAngle === hNextAngle && hNextAngle === mNextAngle) answer--

        sTime++
    }

    return answer;
}
