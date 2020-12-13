from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        answer = []
        queue = deque()
        depth = 0
        queue.append((root, depth))
        stack = [[] for _ in range(50000)]
        while queue:
            
            node, depth = queue.popleft()
            if node is not None:
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))
                stack[depth].append(node.val)
        # print(stack)
        return [i for i in stack if i != []]