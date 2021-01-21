class Solution:
    def groupAnagrams(self, strs):
        dic = {}
        for s in strs:
            ordered_s = "".join(sorted(s))
            if ordered_s in dic:
                dic[ordered_s].append(s)
            else:
                dic[ordered_s] = [s]
        ans = []
        for d in dic.values():
            ans.append(d)
        return ans


s = Solution()
s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
