def solution(friends, gifts):
    # 각 사람별 인덱스 값
    f_idx= {v:i for i, v in enumerate(friends)}
    # 받는 선물 개수 배열
    answer = [0] * len(friends)
    # 각 사람별 선물 지수 배열
    n_dict = [0] * len(friends)
    # 각 사람별로 다른 사람들에게 준 선물 개수 나타낸 배열
    gt_dict = [[0] * len(friends) for i in range(len(friends))]
    
    # 주고받은 선물 개수 업데이트
    for gift in gifts:
        give, take = gift.split()
        gt_dict[f_idx[give]][f_idx[take]] += 1

    # 선물 지수 계산 및 업데이트
    for i in range(len(friends)):
        # i의 선물 지수 = i가 준 선물 개수 - i가 받은 선물 개수
        n_dict[i] = sum(gt_dict[i]) - sum([k[i] for k in gt_dict])

    # 선물 비교를 통해 받는 선물 업데이트
    for i in range(len(friends)):
        for j in range(len(friends)):
            # 준 것 > 받은 것이면 다음달에 +1
            if gt_dict[i][j] > gt_dict[j][i]: answer[i] += 1
            # 주고 받은 것이 같지만 선물 지수가 더 높으면 다음달에 +1
            elif gt_dict[i][j] == gt_dict[j][i]:
                if n_dict[i] > n_dict[j]: answer[i] += 1

    return max(answer)