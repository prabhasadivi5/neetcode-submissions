"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


#we are given an adjacency list, and we have to return a List of the nodes. 
#what I can do is add the nodes to a List as we go, and return the List at the end.
#the logic Should be pretty simple: 
#1) iterate through the adjacency List. If the Node is not already in the graph, add it
#2) The issue is clear -> we need access to the neighbor nodes whenever we add it to the neighbor list -> if we dont, we have no idea how to make neighbor
#3)so say we just made node 1 -> we look at the nrighbors list (2). Since two is not in the dictionary, we create node 2, and add it to the dictionary (int -> Node)
#4) then we add ones neighbors. 
#5) Then we go to two, see its already in teh dictionary, then neighbor 1 already there, so we add that neighbor
#6) After populating every node and its neighbors, we add it to the ret array


# Algo 
#1) declare dictionary
#2) start with the starting node, and do a dfs. If the neighbor is in the dictionary (it wont), populate both ways and process the neighbor
#3) dfs on the neighbor, populate it as well, store in the dict 
#5) return 0 
#6) add the node to ret, repeat
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        processedNodes = set()
        nodesDict = defaultdict(Node)
        if not node:
            return None
        
    
        def dfs(prevNode, currNode):
            processedNodes.add(currNode.val)
            if currNode.val not in nodesDict:
                newNode = Node(currNode.val)
                nodesDict[currNode.val] = newNode

            #we dont want to come back to prev node either. 
            for neighbor in currNode.neighbors:
                if neighbor.val not in processedNodes and (not prevNode or neighbor.val != prevNode.val and currNode.val):
                    dfs(currNode, neighbor)
                nodesDict[currNode.val].neighbors.append(nodesDict[neighbor.val])
        dfs(None, node)
        return nodesDict[1]
            



        
       
        