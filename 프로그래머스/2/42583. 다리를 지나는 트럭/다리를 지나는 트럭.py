def solution(bridge_length, weight, truck_weights):
    t = 0
    on = []
    while truck_weights or on:
        for i, v in enumerate(on):
            on[i] = (v[0], v[1] + 1)
        on = list(filter(lambda x: x[1] < bridge_length + 1, on))

        weight_sum = 0
        for v in on: weight_sum += v[0]

        if truck_weights:
            if weight_sum + truck_weights[0] <= weight:
                on.append((truck_weights.pop(0), 1))
        t += 1

    return t