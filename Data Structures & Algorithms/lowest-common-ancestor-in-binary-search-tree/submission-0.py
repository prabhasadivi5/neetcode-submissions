# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #initial thought is a bfs where we store by level.
        #we can use bst property. Cant we keep going down-> if one is to the left, and one is to the right, we have it
        #if both to the left we keep going left, if right we go right
        #no parents. 
        #basic idea is to go all the way down to both and then trace backwards from them to see common ancestor
        #dfs to p. Then store p. Once we do this, we can construct the path by working our way down.
        # its just hte node where p > and q is greater or q is greater and p is less. If they are both less, we go left

        curr = root
        while (p.val < curr.val and q.val < curr.val) or (p.val >curr.val and q.val > curr.val):
            if p.val > curr.val:
                curr = curr.right
            else:
                curr = curr.left
        return curr
