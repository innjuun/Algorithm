import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) >= 2:
        hot = heapq.heappop(scoville)
        second_hot = heapq.heappop(scoville)
        if hot >= K:
            return answer
        heapq.heappush(scoville, hot + (second_hot * 2))
        answer += 1
    if heapq.heappop(scoville) >= K:
        return answer
    return -1