# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_parent = root
        y_parent = root
        x_depth = -99
        y_depth = -98
        
        def dfs(root, x, y, depth, parent):
            if not root:
                return
            if root.val == x:
                x_parent = parent
                x_depth = depth
            if root.val == y:
                y_parent = parent
                y_depth = depth
            dfs(root.left, x, y, depth+1, root)
            dfs(root.right, x, y, depth+1, root)
        
        dfs(root, x, y, 0, None)
        return (x_parent!=y_parent) and (x_depth==y_depth)

# time complexity - O(n) as in worst case we traverse every node

# space complexity - O(1), no auxillary data structure used

# all test cases passed