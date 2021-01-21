# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = []
    stack = []

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.ans = []
        self.stack = []
        if not root:
            return []

        def dfs(total, node):

            if not node:
                return
            if node.left is None and node.right is None:

                if sum == total + node.val:
                    self.ans.append(self.stack[:] + [node.val])
                return
            self.stack.append(node.val)
            dfs(total + node.val, node.left)
            self.stack.pop()
            self.stack.append(node.val)
            dfs(total + node.val, node.right)
            self.stack.pop()

        dfs(0, root)

        return self.ans
