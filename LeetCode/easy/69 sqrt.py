# brute force


class Solution:
    def mySqrt(self, x: int) -> int:

        for i in range(2 ** 16):
            if i ** 2 > x:
                return i - 1


# binary search


class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x

        while start <= end:
            mid = (start + end) // 2
            if mid ** 2 < x:
                start = mid + 1
            elif x < mid ** 2:
                end = mid - 1
            else:
                return mid
        return end
