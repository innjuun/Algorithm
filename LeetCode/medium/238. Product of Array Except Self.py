class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1] * len(nums)
        backward = [1] * len(nums)
        forward[0] = nums[0]
        backward[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(1, len(nums)):
            forward[i] = forward[i - 1] * nums[i]

        for i in range(len(nums) - 2, 0, -1):
            backward[i] = backward[i + 1] * nums[i]

        ret = [1] * len(nums)
        for i in range(1, len(nums) - 1):
            ret[i] = forward[i - 1] * backward[i + 1]
        ret[0] = backward[1]
        ret[len(nums) - 1] = forward[len(nums) - 2]
        return ret


# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1] * len(nums)
        forward[0] = nums[0]
        for i in range(1, len(nums)):
            forward[i] = forward[i - 1] * nums[i]

        r = 1
        for i in range(len(nums) - 1, 0, -1):
            forward[i] = forward[i - 1] * r
            r = r * nums[i]
        forward[0] = r
        return forward
