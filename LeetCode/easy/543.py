# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0

        def get_max_depth(node):
            if node is None:
                return 0
            left = get_max_depth(node.left)
            right = get_max_depth(node.right)
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1

        get_max_depth(root)
        return self.ans
