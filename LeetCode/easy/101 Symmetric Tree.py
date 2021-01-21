# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False

        if t1.val == t2.val:
            outer_mirror = self.isMirror(t1.left, t2.right)
            inner_mirror = self.isMirror(t1.right, t2.left)
            return outer_mirror and inner_mirror
        else:
            return False
