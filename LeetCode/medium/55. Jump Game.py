
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        indexes = [False for _ in nums]
        indexes[0] = True
        for i, n in enumerate(nums):
            if n == 0:
                continue
            if indexes[i] is False:
                continue


            for j in range(n, 0, -1):
                if (i + j) > len(nums):
                    return True
                if self.in_range(indexes, i+j):
                    if indexes[i + j] == False:  
                        indexes[i + j] = True

                    else:
                        break
                else:
                    continue
        # print(indexes)
        return indexes[-1]
    
    def in_range(self, li, index):
        try:
            li[index]
        except:
            return False
        return True