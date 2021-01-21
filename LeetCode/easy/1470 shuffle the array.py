from collections import deque


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        q1 = deque(nums[:n])
        q2 = deque(nums[n:])
        li = []
        for i in range(n):
            li.append(q1.popleft())
            li.append(q2.popleft())

        return li
