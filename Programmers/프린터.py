from collections import deque


def solution(priorities, location):
    queue = deque([(p, i) for (i, p) in enumerate(priorities)])

    print(queue)
    answer = 0
    while queue:
        left = queue.popleft()
        if any(left[0] < p for (p, i) in queue):
            queue.append(left)
        else:
            answer += 1
            if left[1] == location:
                return answer
