# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #first simply a left helper and a right helper
        #need to track the rightp
        #store minimum and maximum parents 
        


        def validHelper(root, minimum, maximum):
            if not root:
                return True
            if root.val >= maximum or root.val <= minimum:
                return False
            if not root.left and not root.right: 
                return True
            
            if root.left and root.right:
                return validHelper(root.right, root.val, maximum) and validHelper(root.left, minimum, root.val)
            if root.left:
                return validHelper(root.left, minimum, root.val)
            else:
                return validHelper(root.right, root.val, maximum)
        if not root:
            return True
        return validHelper(root.left, -99999, root.val) and validHelper(root.right, root.val, 99999)


        