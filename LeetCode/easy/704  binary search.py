# recursive


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarysearch(nums, start, end, target):
            if start <= end:
                mid = (start + end) // 2

                if nums[mid] == target:
                    answer.append(mid)
                    print(mid)
                    return
                elif nums[mid] < target:
                    binarysearch(nums, mid + 1, end, target)
                else:
                    binarysearch(nums, 0, mid - 1, target)

        answer = []
        binarysearch(nums, 0, len(nums) - 1, target)
        if answer:
            return answer.pop()
        else:
            return -1


# iterative


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start = 0
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
