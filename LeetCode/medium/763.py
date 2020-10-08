class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        max_dict = {num: index for index, num in enumerate(S)}

        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, max_dict[c])
            if j == i:
                ans.append(i - anchor + 1)
                anchor = i + 1
        return ans


# helped from solution, need to be re-solved
