# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    flag = False
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        def travel(total, node):
            if node and node.left is None and node.right is None:
                if total + node.val == sum:
                    self.flag = True
                return
            if not node:
                return
                
            travel(total + node.val, node.left)
            travel(total + node.val, node.right)
        
        travel(0, root)
        
        return self.flag