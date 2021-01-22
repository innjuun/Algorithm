class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        min_length = min(len(x) for x in strs)
        for i in range(min_length):
            char = strs[0][i]

            for j in range(len(strs)):
                if strs[j][i] == char:
                    continue
                else:
                    return strs[0][:i]

        return strs[0][:min_length]
                