# wrong

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        sum_by_depth = [0] * 1000
        queue = deque()
        
        queue.append((root, 0))
        
        while queue:
            node, depth = queue.popleft()
            if node is not None:
                sum_by_depth[depth] += node.val
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))
        
        
        dp = [0] * 1000
        for i in range(1000):
            dp[i] = max((sum_by_depth[i] + dp[i-2], dp[i-1]))
        
        print(dp)
        return max(dp)
    
    
# recursion

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        def helper(node):
            if not node:
                return (0, 0)
            left_rob = helper(node.left)
            right_rob = helper(node.right)
            
            rob = node.val + left_rob[1] + right_rob[1]
            not_rob = max(left_rob) + max(right_rob)
            
            return [rob, not_rob]
        
        return max(helper(root))
            