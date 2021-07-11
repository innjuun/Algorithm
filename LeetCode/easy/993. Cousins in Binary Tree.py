# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.li = []
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.x = x
        self.y = y
        self.inorder(root, 0)
        if len(self.li) < 2:
            return False
        return self.li[0][0] != self.li[1][0] and self.li[0][1] == self.li[1][1]

    def inorder(self, root, depth):
        if root is None:
            return

        if root.left is not None:
            if root.left.val == self.x or root.left.val == self.y:
                self.li.append((root.val, depth + 1))
            self.inorder(root.left, depth + 1)

        if root.right is not None:
            if root.right.val == self.x or root.right.val == self.y:
                self.li.append((root.val, depth + 1))
            self.inorder(root.right, depth + 1)