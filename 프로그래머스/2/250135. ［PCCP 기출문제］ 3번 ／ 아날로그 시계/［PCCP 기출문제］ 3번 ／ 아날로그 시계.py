def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    sTime = h1 * 3600 + m1 * 60 + s1
    eTime = h2 * 3600 + m2 * 60 + s2  

    if sTime == 0 * 3600 or sTime == 12 * 3600: answer += 1

    while sTime < eTime:
        hCurAngle = sTime / 120 % 360
        mCurAngle = sTime / 10 % 360
        sCurAngle = sTime * 6 % 360

        hNextAngle = 360 if (sTime + 1) / 120 % 360 == 0 else (sTime + 1) / 120 % 360
        mNextAngle = 360 if (sTime + 1) / 10 % 360 == 0 else (sTime + 1) / 10 % 360
        sNextAngle = 360 if (sTime + 1) * 6 % 360 == 0 else (sTime + 1) * 6 % 360

        if sCurAngle < hCurAngle and sNextAngle >= hNextAngle: answer += 1
        if sCurAngle < mCurAngle and sNextAngle >= mNextAngle: answer += 1
        if sNextAngle == hNextAngle and hNextAngle == mNextAngle: answer -= 1

        sTime += 1
    
    return answer