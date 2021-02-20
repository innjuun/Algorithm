from collections import defaultdict
def solution(S):
    S = [list(s) for s in S]
    # write your code in Python 3.6
    
    
    for index, strs in enumerate(zip(*S)):
        dic = defaultdict(int)
        for i, string in enumerate(strs):
            if string in dic:
                return [dic[string], i, index]
            dic[string] = i

    return []   

solution(['abc', 'bca', 'dbe'])