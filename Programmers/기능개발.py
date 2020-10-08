def solution(progresses, speeds):
    answer = []
    cnt = 0
    while progresses:
        while progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
            if not progresses:
                break
        if cnt != 0:
            answer.append(cnt)

        if progresses:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
        cnt = 0

    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
solution(progresses, speeds)