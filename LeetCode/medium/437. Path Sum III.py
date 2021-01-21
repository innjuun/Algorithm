# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        self.answer = 0
        if not root:
            return 0

        def dfs(total, node):
            sum_from_node(total, node)
            if node.left is not None:
                dfs(total, node.left)
            if node.right is not None:
                dfs(total, node.right)

        def sum_from_node(total, node):

            if target == total + node.val:
                self.answer += 1
            if node.left is not None:
                sum_from_node(total + node.val, node.left)
            if node.right is not None:
                sum_from_node(total + node.val, node.right)

        dfs(0, root)

        return self.answer
