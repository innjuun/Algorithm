class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = []
        for i in range(n + 1):
            ret.append(str(bin(i)).count("1"))
        return ret

class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = [0]
        cache = [0]
        i = 1
        while i <= n:
            
            cache = cache + [d + 1 for d in cache]
            i *= 2
        return cache[:n + 1]