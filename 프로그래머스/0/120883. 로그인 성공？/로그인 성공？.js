function solution(id_pw, db) {
    const [ uId, uPw ] = id_pw;
    for (const [ id, pw ] of db) {
        if (uId === id && uPw === pw) return "login";
        else if (uId === id && uPw !== pw) return "wrong pw";
    }
    return "fail";
}