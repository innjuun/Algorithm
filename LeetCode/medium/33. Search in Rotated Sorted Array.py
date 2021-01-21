class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] < nums[i - 1]:
                index = i
                break
        if nums[index] == target:
            return index

        start = 0
        end = index - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        start = index + 1
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return -1
