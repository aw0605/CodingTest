from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    curWeight = 0
    while len(truck_weights):
        time += 1
        curWeight -= bridge.popleft()

        if curWeight + truck_weights[0] <= weight:
            curWeight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else: bridge.append(0)

    return time + bridge_length