class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ % 2 != 0:
            return False
        self.answer = False
        self.totals = {}

        def dfs(position, total):
            # print(self.totals, self.answer)
            if self.answer:
                return
            self.totals[total] = summ - total == total
            if self.totals[total]:
                self.answer = True

            for i in range(position, len(nums)):

                if self.totals.get(total + nums[i]) is False:
                    continue
                dfs(i + 1, total + nums[i])

        dfs(0, 0)
        return self.answer
