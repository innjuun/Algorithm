from collections import deque
class Solution:
    def numIslands(self, grid):
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        
        def is_valid(x, y):
            return x >= 0 and x < len(grid) and y >= 0  and y < len(grid[0])

        answer = 0
        # visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        
        def dfs(x, y):
            if not is_valid(x, y):
                return
            if grid[x][y] == "0":
                return
            grid[x][y] = "0"
            for i in range(4):
                dfs(x + dx[i], y + dy[i])
            
        def bfs(queue):
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    if is_valid(x + dx[i], y + dy[i]) and grid[x+dx[i]][y+dy[i]] == "1":
                        queue.append((x+dx[i], y+dy[i]))
                        grid[x+dx[i]][y+dy[i]] = "0"
                        
                
                
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
         
                if grid[i][j] == "1":
                    queue.append((i, j))
                    bfs(queue)
                    answer += 1
                    
        

        return answer
    
li = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
a = Solution()
a.numIslands(li)