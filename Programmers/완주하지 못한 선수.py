def solution(participant, completion):
    ret = dict()
    for person in participant:
        if ret.get(person):
            ret[person] += 1
        else:
            ret[person] = 1

    for person in completion:
        if ret[person] > 1:
            ret[person] -= 1
        else:
            ret.pop(person)
    return ret.popitem()[0]
