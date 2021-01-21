# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(root):
            if root.left is not None:
                inorder(root.left)
            # print(root.val)
            num.append(root.val)
            if root.right is not None:
                inorder(root.right)

        num = []
        inorder(root)
        return num[k - 1]
