class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        def is_valid(x, y, matrix):
            if x >= 0 and x < n and y >=0 and y < n and matrix[x][y] == 0:
                return True
            return False
        
        i = 0
        j = 0
        cnt = 1
        def is_complete(matrix):
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    if matrix[i][j] == 0:
                        return False
            return True
        while not is_complete(matrix):
            

            # print(i, j, matrix)
            while is_valid(i, j+1, matrix):
                matrix[i][j] = cnt
                cnt += 1
                j += 1
            while is_valid(i+1, j, matrix):
                matrix[i][j] = cnt
                cnt += 1
                i += 1
            while is_valid(i, j-1, matrix):
                matrix[i][j] = cnt
                cnt += 1
                j -= 1
            while is_valid(i-1, j, matrix):
                matrix[i][j] = cnt
                cnt += 1
                i -= 1
            if not is_valid(i, j+1, matrix) and not is_valid(i+1, j, matrix) and not is_valid(i, j-1, matrix) and not is_valid(i-1, j, matrix):
                matrix[i][j] = cnt
            
        return matrix