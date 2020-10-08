class Solution:
    def climbStairs(self, n: int) -> int:
        li = [0 for _ in range(n)]
        
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            li[0] = 1
            li[1] = 2
            for i in range(2, n):
                li[i] = li[i-1] + li[i-2]

            return li[n-1]