class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
       #return the number of connected components
       #just a simple dfs, add to visited set, if already visited, we dont run the dfs
       #logic
       #1)adjacency list of sets -> each node has a set if nodes that its connected to -> undirected so bothways
       #2)start at any node (just say zero)
       #3)add that node and all extended nrighbors to set
       #4)Counter += 1, and then, go to the next node -> 1
       #5) check if thats in the set, do the neighbors, etc. 
       #6) keep going until the end

        adjacencyList = defaultdict(set)
        for firstNode, secondNode in edges:
            adjacencyList[firstNode].add(secondNode)
            adjacencyList[secondNode].add(firstNode)

        totalComponents = 0
        visited = set()

        def dfs(n):
            for neighbor in adjacencyList[n]:
                if neighbor in visited:
                    continue
                else:
                    visited.add(neighbor)
                    dfs(neighbor)


        counter = 0
        for i in range(n):
            if i in visited: 
                continue
            counter += 1
            visited.add(i)
            dfs(i)
        return counter 




        