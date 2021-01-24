# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         if len(text1) < len(text2):
#             shorter_text = text1
#             longer_text = text2
#         else:
#             shorter_text = text2
#             longer_text = text1
        
#         answer = 0

#         for i in range(len(shorter_text)):
#             j = i
#             k = 0
#             cnt = 0
#             while k < len(longer_text) and j < len(shorter_text):
#                 if shorter_text[j] == longer_text[k]:
#                     j += 1
#                     k += 1
#                     cnt += 1
#                 else:
#                     k += 1
            
            
#             answer = max(cnt, answer)
            
#         return answer
# #             for j in range(i, len(shorter_text)):
                

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                print(i, j)
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # print(dp)
        return dp[len(text1)][len(text2)]

            