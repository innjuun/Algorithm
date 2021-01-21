# brute force


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(len(nums)):
            if nums[i] == target:
                answer.append(i)
        if answer:
            return [answer[0], answer[-1]]
        else:
            return [-1, -1]


# binary search


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1

        def find_first_index(nums, target, start, end):
            index = -1

            while start <= end:
                mid = (start + end) // 2

                if nums[mid] >= target:
                    end = mid - 1
                else:
                    start = mid + 1
                if nums[mid] == target:
                    index = mid
                # print(start, end)
            return index

        def find_last_index(nums, target, start, end):
            index = -1

            while start <= end:
                mid = (start + end) // 2

                if nums[mid] <= target:
                    start = mid + 1
                else:
                    end = mid - 1
                if nums[mid] == target:
                    index = mid
            return index

        a = find_first_index(nums, target, start, end)
        b = find_last_index(nums, target, start, end)
        return [a, b]
