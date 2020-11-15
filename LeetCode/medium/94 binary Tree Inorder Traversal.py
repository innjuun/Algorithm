# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# using recursion
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
    
    
# iterative solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        

        node = root
        stack.append(node)
        while stack:
            
            while node is not None:    
                stack.append(node.left)
                node = node.left
            node = stack.pop()
            if node is not None:
                res.append(node.val)
       
                stack.append(node.right)
                node = node.right
            
            
        return res

#optimize

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        

        node = root
        while stack or node:
            
            while node:    
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right

            
        return res