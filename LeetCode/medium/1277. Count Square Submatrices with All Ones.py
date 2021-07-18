# brute force(time limit exceeded)
class Solution(object):

    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.matrix = matrix
        self.max_j = len(self.matrix[0]) - 1
        self.max_i = len(self.matrix) - 1
        ret = 0
        for length in range(min(self.max_i, self.max_j) + 1):
            for i in range(self.max_i + 1):
                for j in range(self.max_j + 1):
                    if self.is_square(i, j, length):
                        ret += 1
        
        return ret
        
    def is_in_range(self, i, j):
        return self.max_j >= j and self.max_i >= i
    
    def is_one(self, i, j):
        return self.is_in_range(i, j) and self.matrix[i][j] == 1
    
    def is_square(self, i, j, length):
        for m in range(length + 1):
            for n in range(length + 1):
                if not self.is_one(i + m, j + n):
                    return False
                
        return True
    
Solution().countSquares([
  [1,0,1],
  [1,1,0],
  [1,1,0]
])

# dp

class Solution(object):

    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        dp = [[0 for num in line] for line in matrix]
        dp[0] = [num for num in matrix[0]]
        for i in range(len(matrix)):
            dp[i][0] = matrix[i][0]
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j]:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                
        return sum(sum(line) for line in dp)