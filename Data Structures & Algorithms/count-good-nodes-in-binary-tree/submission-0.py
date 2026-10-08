# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, currmax):
            if not root: 
                return 0
            if root.val >= currmax: 
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
            
            else: 
                return dfs(root.left, currmax) + dfs(root.right, currmax)
        return dfs(root, root.val)

            
