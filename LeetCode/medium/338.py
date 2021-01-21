class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0] * (num * 2)
        if num == 0:
            return [0]

        ans[0] = 0
        i = 0
        while True:
            if 2 ** i > num:
                break
            i += 1

        for i in range(1, i + 1):
            for j in range(2 ** (i - 1), 2 ** i):
                ans[j] = ans[j - (2 ** (i - 1))] + 1
        return ans[: num + 1]
