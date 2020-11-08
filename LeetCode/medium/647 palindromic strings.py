class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_palindrome(val):
            return val[::-1] == val

        answer = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                # print(s[i:j+1])
                if is_palindrome(s[i:j+1]):
                    answer += 1

        return answer
    
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
    
        j = 2
        while j < len(s):  
            for i in range(len(s)-j):
                if s[i] == s[i+j] and dp[i+1][i+j-1] is True:
                    dp[i][i+j] = True
            j += 1
        return (sum(x.count(True) for x in dp))