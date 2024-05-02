function solution(emergency) {
    const emergencyArr = [...emergency].sort((a,b) => b-a);
    return emergency.map((v) => v = emergencyArr.indexOf(v)+1);
}