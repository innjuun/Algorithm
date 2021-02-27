# from itertools import combinations
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         answer = []
#         for i in range(len(nums) + 1):
#             for c in combinations(nums, i):
#                 answer.append(list(c))
#         return answer

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         answer = [[]]

#         # for i in range(len(nums)):
#         #     for j in range(len(answer)):
#         #         answer.append(answer[j] +[nums[i]])
#         # is same as
#         for num in nums:
#             answer += [curr + [num] for curr in answer]
#         return answer

from itertools import combinations


# class Solution:
#     def subsets(self, nums):
#         def dfs(index, stop, nums):
#             if index == stop:
#                 answer.append(stack[:])
#                 return

#             for i in range(index, len(nums)):
#                 # if visited[i]:
#                 #     continue
#                 # visited[i] = True
#                 stack.append(nums[i])
#                 dfs(i + 1, stop, nums)
#                 visited[i] = False
#                 stack.pop()

#         answer = []
#         for i in range(len(nums) + 1):
#             visited = [False] * len(nums)
#             stack = []
#             dfs(0, i, nums)

#         return answer


# a = Solution()
# a.subsets([1, 2, 3])

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(stop, index):
            if stop == len(stack):
                answer.append(stack[:])
                return

            for i in range(index, len(nums)):

                stack.append(nums[i])

                dfs(stop, i + 1)
                stack.pop()

        answer = []
        stack = []
        for i in range(len(nums) + 1):
            dfs(i, 0)
        return answer
    


class Solution:
    def subsets(self, nums):
        answer = [[]]
        for i in range(len(nums) + 1):
            
            for ans in answer[:]:
                
                num = ans[:]
                num.append(nums[i])
                answer.append(num)
    

s = Solution()
s.subsets([1,2,3])