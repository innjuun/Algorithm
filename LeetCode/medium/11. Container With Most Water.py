# brute force, time limit exceeded


class Solution:
    def maxArea(self, height: List[int]) -> int:
        dp = [0] * len(height)
        maximum = 0
        for i in range(1, len(height)):
            for j in range(0, i):

                maximum = max(maximum, min(height[i], height[j]) * (i - j))
        return maximum


# two pointer solution


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1

        maximum = 0
        while start <= end:
            maximum = max(maximum, (end - start) * min(height[start], height[end]))

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return maximum
