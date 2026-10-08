class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #originally the graph no cycles and n-1 edges
        #added one edge to the graph, two different verticies from 1-n
        #return the edge that can be removed so the graph is a connected non cyclical 
        #first detect the cycle. and then remove the cycle. 
        #can just use a dfs to detect a cycle with backtracking?


        #so we have a dfs, with recursion. If there is no cycle in the dfs, we return and remove from the stored array
        #if there is a cycle, we return and dont remove 
        #so, 2 -> 1 -> 3 -> 4 -> 1 
        #then we can just take this array, iterate through it, and make a new edges in set 
        #then with that set, we iterate one more time thru edges list from back, if equal, we good
        #the dfs returns True, False. if cycleFound, we return True and backtrack. Otherwise, we remove and keep exploring neighbors
        #its undirected so we need another set to track which edges are already in the DFS?
        adjacencyList = defaultdict(list)
        for firstNode, secondNode in edges:
            adjacencyList[firstNode].append(secondNode)
            adjacencyList[secondNode].append(firstNode)

        dfsVisited = set()
        nodesVisited = set()
        path = []
        def dfs(currNode):
            for nextNode in adjacencyList[currNode]:
                if (nextNode, currNode) in dfsVisited or (currNode, nextNode) in dfsVisited:
                    continue
                if nextNode in nodesVisited:
                    path.append(nextNode)
                    return True 
            
                nodesVisited.add(nextNode)
                dfsVisited.add((currNode, nextNode))
                path.append(nextNode)
                if dfs(nextNode) == True:
                    return True
                dfsVisited.remove((currNode, nextNode))
                nodesVisited.remove(nextNode)
                path.pop()
            return False
        path.append(edges[0][0])
        nodesVisited.add(edges[0][0])
        dfs(edges[0][0])
        print(path)


        edgesUsed = set()
        firstFound = False
        repeated = path[len(path)-1]
        for i in range(len(path)-1):
            if not firstFound:
                if path[i] == repeated:
                    firstFound = True
                else:
                    continue
            else:
                edgesUsed.add((path[i], path[i+1]))
                edgesUsed.add((path[i+1], path[i]))

        for i in range(len(edges) - 1, -1, -1):
            first, second = edges[i]

            if (first, second) in edgesUsed or (second, first) in edgesUsed:
                return edges[i]
        return [0,0]

                
        