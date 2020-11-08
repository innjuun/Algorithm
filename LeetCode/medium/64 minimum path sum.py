# timeout

# from collections import deque
# INF = int(1e9)
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         pi = [0, 1]
#         pj = [1, 0]
#         dp = [[INF for _ in range(len(grid[0]))] for _ in range(len(grid))]

#         def is_valid_direction(i, j):
#             if  i < len(grid) and j  < len(grid[0]):
#                 return True
#             return False
#         queue = deque()
#         row  = col = 0
#         dp[0][0] = grid[0][0]
#         queue.append((0, 0))

#         while queue:
#             i, j = queue.popleft()
#             # print(queue)
#             for t in range(2):
#                 if is_valid_direction(i+pi[t], j+pj[t]):
#                     # print(i+pi[t], j+pj[t])
#                     dp[i+pi[t]][j+pj[t]] = min(dp[i][j] + grid[i+pi[t]][j+pj[t]], dp[i+pi[t]][j+pj[t]])
#                     queue.append((i+pi[t], j+pj[t]))
#         # print(dp)
#         return dp[len(grid)-1][len(grid[0])-1]

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        if ROW == COL == 1:
            return grid[0][0]
        dp = [[0 for _ in range(COL)] for _ in range(ROW)]
        
        for i in range(ROW):
            for j in range(COL):
                dp[i][j] = grid[i][j]
                if i == 0:
                    dp[i][j] += dp[i][j-1]
                elif j == 0:
                    dp[i][j] += dp[i-1][j] 
                else:
                    dp[i][j] += min(dp[i][j-1], dp[i-1][j])

        return (dp[ROW-1][COL-1])