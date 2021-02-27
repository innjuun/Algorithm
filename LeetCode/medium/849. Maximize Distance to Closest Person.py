from collections import OrderedDict
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        maximum = 0
        pos = 0
        for i, num in enumerate(seats):
            if seats[i] == 1:
                continue
            left = 0
            right = 0
            while (i - left >=0 and seats[i - left] == 0):
                left += 1
            if i - left == -1:
                left = 1000000
            while (i + right < len(seats) and seats[i + right] == 0):
                right += 1
            if i + right == len(seats):
                right = 1000000
            # print(i, left, right)
            distance = min(left, right)
            if distance > maximum:
                maximum = distance
                pos = i

        return maximum
