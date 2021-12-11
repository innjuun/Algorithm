from collections import defaultdict
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = defaultdict(int)
        for char in s:
            dic[char] += 1
            
        print(dic)
        new_dic = defaultdict(list)
        for key, value in dic.items():
            new_dic[value].append(key)
        
        
        ret = []
        for num, char in sorted(new_dic.items(), reverse=True):
            for c in char:
                ret.append(c * num)
        return ''.join(ret)