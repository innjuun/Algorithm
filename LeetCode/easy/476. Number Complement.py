class Solution:
    def findComplement(self, num: int) -> int:
        for i in range(32):
            if 2**i > num:
                return 2**i - 1 - num