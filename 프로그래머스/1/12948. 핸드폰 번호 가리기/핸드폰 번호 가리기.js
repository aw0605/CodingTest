function solution(phone_number) {
    const nlen = phone_number.length;
    return "*".repeat(nlen-4) + phone_number.slice(nlen-4, nlen);
}