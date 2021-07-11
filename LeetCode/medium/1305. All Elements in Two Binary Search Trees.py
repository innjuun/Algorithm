# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.li = []
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.ascend(root1)
        self.ascend(root2)
        return sorted(self.li)
    
    def ascend(self, root: TreeNode):
        if root is None:
            return
        if root.left is not None:
            self.ascend(root.left)
        
        self.li.append(root.val)
        if root.right is not None:
            self.ascend(root.right)