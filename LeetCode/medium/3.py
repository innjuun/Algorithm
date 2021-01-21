# brute force


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        maximum = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if self.allUnique(s, i, j):
                    maximum = max(maximum, j - i)

        return maximum

    def allUnique(self, s, start, end):
        sett = set()
        for i in range(start, end):
            if s[i] in sett:
                return False
            else:
                sett.add(s[i])
        return True


# sliding window


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()

        answer = i = j = 0

        while i < len(s) and j < len(s):
            if s[j] not in sett:
                sett.add(s[j])
                j += 1
                answer = max(answer, j - i)
            else:
                sett.remove(s[i])
                i += 1

        return answer
