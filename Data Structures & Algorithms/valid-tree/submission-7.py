class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #tree means theres no cycles. 
        #the edges are undirected, so we do a dfs, store the path, and if the path is not in the dfs, we leave

        #1) make the adjacency matrix and a visited(completed) set 
        #2) iterate through every edge 1-n. -> in every dfs, we need a temp visited as well as a completed. if a node is visited, we just dont visit it again (since the dfs is verified)
        #if its in the temp set, we are returning false. 
        #at the end of the dfs, remove the node from the visited set and add it to completed
        #then return true for the dfs
        #in each dfs, we need an or, so we iterate through all of the neighbors, if any of them return false, return false. Otherwise, return True
        
        





        adj = defaultdict(list)
        for val in edges:
            i = val[0]
            j = val[1]
            adj[i].append(j)
            adj[j].append(i)
        visited = set()
        curr = set()

        def dfs(node, prev):
            
            curr.add(node)
            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                if neighbor in visited:
                    continue
                if neighbor in curr:
                    return False
                
                if dfs(neighbor, node) == False:
                    return False
            visited.add(node)
            curr.remove(node)
            return True




        
        temp = dfs(0,-1)
        if len(visited) != n:
            return False
        return temp

    

        
