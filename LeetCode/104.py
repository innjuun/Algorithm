class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root) -> int:
    global depth, max_depth
    if root:
        depth += 1
        if depth >= max_depth:
            max_depth = depth
    else:
        depth -= 1
        return


    maxDepth(root.left)
    maxDepth(root.right)
    
    return max_depth

depth = 0
max_depth = 0
maxDepth([3,9,20,None, None,15,7])