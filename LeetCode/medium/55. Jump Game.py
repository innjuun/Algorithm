def canJump(nums) -> bool:
    
    n = len(nums)
    
    if n==1:
        return True
    
    dp = [0]*(n)
    
    prev_best = n-1
    
    dp[n-1] = 1
    
    for i in range(n-2, -1, -1):
        print(dp)
        step = nums[i]
        
        if (i+step)>=prev_best:
            
            dp[i] = 1
            prev_best = i
    
    print(dp)
    if dp[0]:
        return True
    
    return False

canJump([2,3,1,1,4])