from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    crossing = deque()
    answer = 1
    while truck_weights or crossing:
        answer += 1
        total_weight = sum(i for i, j in crossing)
        if truck_weights and weight >= (total_weight + truck_weights[0]):
            crossing.append([truck_weights.popleft(), bridge_length])
        for i in range(len(crossing)):
            crossing[i][1] -= 1
        while crossing and crossing[0][1] == 0:
            crossing.popleft()
    return answer


solution(1, 10, [6])
