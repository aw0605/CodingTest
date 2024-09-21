import math

def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    organization = {}

    for idx in range(len(enroll)):
        organization[enroll[idx]] = (referral[idx], idx)

    for idx in range(len(seller)):
        cp, ca = seller[idx], amount[idx] * 100
        up, ci = organization[cp]

        sh = math.floor(ca * 0.1)

        answer[ci] += ca - sh

        while not (sh == 0 or up == "-"):
            ca = sh
            up, ci = organization[up]
            sh = math.floor(ca * 0.1)

            answer[ci] += ca - sh

    return answer