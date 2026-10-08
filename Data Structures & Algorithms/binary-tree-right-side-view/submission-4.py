from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #right side of a binary tree.
        #the rightmost on each level, since its each level that screams bfs
        #we can go bfs and rightmost would be the last added if we go left first
        ret = []
        myq = deque()
        if root:
            myq.append(root)
        levelsize = 0
        levelcounter = 0
        while myq:
            levelsize = len(myq)
            levelcounter = 0
            for i in range(len(myq)):
                curr = myq.popleft()
                if curr.left:
                    myq.append(curr.left)
                if curr.right:
                    myq.append(curr.right)
                levelcounter += 1
                if(i == levelsize - 1):
                    ret.append(curr.val)
        return ret




        