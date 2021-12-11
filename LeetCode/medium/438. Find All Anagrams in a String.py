# import copy


# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         dic = {
#             "a": 0,
#             "b": 0,
#             "c": 0,
#             "d": 0,
#             "e": 0,
#             "f": 0,
#             "g": 0,
#             "h": 0,
#             "i": 0,
#             "j": 0,
#             "k": 0,
#             "l": 0,
#             "m": 0,
#             "n": 0,
#             "o": 0,
#             "p": 0,
#             "q": 0,
#             "r": 0,
#             "s": 0,
#             "t": 0,
#             "u": 0,
#             "v": 0,
#             "w": 0,
#             "x": 0,
#             "y": 0,
#             "z": 0,
#         }
#         if len(s) < len(p):
#             return []
#         dic2 = copy.deepcopy(dic)
#         for i in p:
#             dic[i] += 1
#         start = 0
#         end = 0
#         answer = []
#         for i in range(len(p)):
#             dic2[s[end]] += 1
#             end += 1
#         end -= 1
#         while end < len(s):
#             try:
#                 # print(answer, start, end)
#                 if dic == dic2:
#                     answer.append(start)
#                 dic2[s[start]] -= 1
#                 start += 1

#                 end += 1
#                 dic2[s[end]] += 1
#             except:
#                 pass

#         return answer

from collections import defaultdict
import string
class Solution:
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        ret = []
        length = len(p)
        dic = {lowercase: 0 for lowercase in string.ascii_lowercase}
        subdic = {lowercase: 0 for lowercase in string.ascii_lowercase}
        for i in p:
            dic[i] += 1
        
        for i in range(length):
            subdic[s[i]] += 1
        
        if subdic == dic:
            ret.append(0)
        try:
            for i in range(1, len(s)):
                subdic[s[i + length - 1]] += 1
                subdic[s[i - 1]] -= 1
                if subdic == dic:
                    ret.append(i)
        except:
            pass

        return ret


Solution().findAnagrams("cbaebabacd", "abc")