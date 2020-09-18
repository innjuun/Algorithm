def solution(answers):
    a = [1, 2, 3, 4, 5] * 2001
    b = [2, 1, 2, 3, 2, 4, 2, 5] * 1300
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1001
    li = [0, 0, 0]
    dic = {"1": 0, "2": 0, "3": 0}
    for i in range(len(answers)):
        if a[i] == answers[i]:
            dic["1"] += 1
        if b[i] == answers[i]:
            dic["2"] += 1

        if c[i] == answers[i]:
            dic["3"] += 1
    maximum = max(dic.values())
    ans = []
    for key, value in dic.items():
        if value == maximum:
            ans.append(int(key))
    return sorted(ans)
