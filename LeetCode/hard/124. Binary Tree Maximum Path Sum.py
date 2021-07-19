# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.answer = -9999999
        
        self.get_maximum(root)
        return self.answer
        
    def get_maximum(self, root):
        if root is None:
            return 0
        
        left_max = max(self.get_maximum(root.left), 0)
        right_max = max(self.get_maximum(root.right), 0)
        
        canbe_answer = left_max + right_max + root.val
        self.answer = max(self.answer, canbe_answer)

        return max(left_max, right_max) + root.val