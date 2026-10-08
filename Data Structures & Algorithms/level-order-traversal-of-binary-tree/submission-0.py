
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #return everything in order based on level 
        #this is basically a bfs, so we would use a queue
        #create the return array
        #create the queue, add the root
        #have a while loop in each where we have a for loop the length of the queue (bfs)
        #in each while iter, make a new array (level of the bfs)
        #from this for loop, we add to the queue based on the level
        #we start over
        ret = []
        queue = deque()
        if root:
            queue.append(root)
        while(queue):
            currLevel = []
            for val in range(len(queue)):
                currNode = queue.popleft()
                currLevel.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            ret.append(currLevel)
        return ret 



        
        
        