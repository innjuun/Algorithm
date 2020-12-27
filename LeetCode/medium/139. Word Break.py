class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.answer = False
        if not wordDict or not s:
            return False
        word_dict = set(wordDict)
        cache = {}
        if len(s) == 1:
            if "".join(word_dict) == s:
                return True
            else:
                return False

        def dfs(curr_s, index):
            if index == len(s) - 1:
                self.answer = True
                return
            for i in range(len(s)):
                print(i, curr_s[:i+1])
                if curr_s[:i+1] in word_dict:
                    
                    
                    dfs(curr_s[i+1:], i)
            
        dfs(s, 0)
        
        return self.answer