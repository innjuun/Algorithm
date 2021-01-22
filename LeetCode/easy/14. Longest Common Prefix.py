class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_length = min(len(x) for x in strs)
        answer = ""
        for i in range(min_length):
            char = ""
            flag = True
            for j in range(len(strs)):
                if j == 0:
                    char = strs[j][i]
                    continue
                if strs[j][i] == char:
                    continue
                else:
                    flag = False
                    break
            if flag == True:
                answer += char
            else:
                break
        return answer
                