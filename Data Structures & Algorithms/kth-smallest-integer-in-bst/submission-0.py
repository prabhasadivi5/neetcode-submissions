# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #kth smallest value, so we have to start from the right, calculate the size of the tree on the right, and then if it is that we go thru, if not we stay 
        #if the right subtree is greater, we go right. 
        myarr = []
        def recurse(root, myarr):
            if root == None: 
                return 
            if root.left:
                recurse(root.left, myarr)
            
            myarr.append(root.val)
            recurse(root.right, myarr)
        
        recurse(root, myarr)
        return myarr[k-1]

        
        