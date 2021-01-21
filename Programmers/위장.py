def solution(clothes):
    dic = {}
    for cloth in clothes:
        for clo in cloth[:-1]:
            if not cloth[-1] in dic:
                dic[cloth[-1]] = [clo]
            else:
                dic[cloth[-1]].append(clo)
    answer = 1
    for value in dic.values():
        answer = answer * (len(value) + 1)

    return answer - 1


solution(
    [
        ["yellow_hat", "headgear"],
        ["blue_sunglasses", "eyewear"],
        ["green_turban", "headgear"],
    ]
)
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])
