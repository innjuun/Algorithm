# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def inner(root):
            if root is None:
                return
            inner(root.left)
            ans.append(root.val)
            inner(root.right)
        inner(root)
        return ans