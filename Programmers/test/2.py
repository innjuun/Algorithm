def solution(answers):

    a = [1,2,3,4,5] * 2005
    b = [2,1,2,3,2,4,2,5] * 1300
    c = [3,3,1,1,2,2,4,4,5,5] * 1010
    dic = {'1': 0, '2': 0, '3': 0}
    for i, ans in enumerate(answers):
        if ans == a[i]:
            dic['1'] = dic['1'] + 1
        if ans == b[i]:
            dic['2'] = dic['2'] + 1
        if ans == c[i]:
            dic['3'] = dic['3'] + 1
    max_val = max(dic.values())
    answer = []
    for key, value in dic.items():
        if value == max_val:
            answer.append(key)
    return sorted(answer)

solution([1,3,2,4,2])