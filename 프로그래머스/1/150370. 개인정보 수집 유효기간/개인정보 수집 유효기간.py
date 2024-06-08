def days(date):
    y, m, d = map(int, date.split("."))
    return y * 28 * 12 + m * 28 + d

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire