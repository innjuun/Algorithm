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
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        lasts = {c: i for i, c in enumerate(S)}
        
        partition = 0
        answer = []
        for i, c in enumerate(S):
            partition = max(partition, lasts[c])
            if i == partition:
                answer.append(i - sum(answer) + 1)

        return answer