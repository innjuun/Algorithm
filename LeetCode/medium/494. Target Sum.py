# # dfs, TLE

# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         stack = []
#         count = 0
#         count = []
#         def dfs(index):
#             if index == len(nums):
#                 # print(stack)
#                 if sum(stack) == S:
#                     count.append(1)
#                 return
            
#             stack.append(nums[index])
#             dfs(index + 1)
#             stack.pop()
#             stack.append(-nums[index])
#             dfs(index + 1)
#             stack.pop()
        
#         dfs(0)
#         return sum(count)
    
# # TLE
# class Solution:
#     count = 0
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         stack = []
#         summary = 0
#         def dfs(index, summary):
#             if index == len(nums):
#                 if summary == S:
#                     self.count += 1
#                 return
            
#             dfs(index + 1, summary + nums[index])
            
            
#             dfs(index + 1, summary - nums[index])
        
#         dfs(0, summary)
#         return self.count

class Solution:
    memo = {}
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        summary = 0
        self.memo = {}
        def dfs(index, summary):
            if (index, summary) in self.memo:
                return self.memo[(index, summary)]
            if index == len(nums):
                if summary == S:
                    return 1
                return 0
            
            positive = dfs(index + 1, summary + nums[index])
            negative = dfs(index + 1, summary - nums[index])
            
            self.memo[(index, summary)] = positive + negative
            return self.memo[(index, summary)]
        answer = dfs(0, summary)

        return answer