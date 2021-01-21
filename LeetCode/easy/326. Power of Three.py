class Solution:

            
    def isPowerOfThree(self, n: int) -> bool:
        num = 3**25
        if n > 0 and num % n == 0:
            return True
        return False