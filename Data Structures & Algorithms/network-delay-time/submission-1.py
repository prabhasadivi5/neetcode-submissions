import heapq
from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #given a network of n directed nodes, and a list of directed edges
        #you are given edges and nodes. We want the minimum time for all nodes
        #can just run djikstras bfs 
        #first created a adjacency matrix, have a visited, we can use a dictionary of arrays
        adj = {}
        for first, second, weight in times:
            if not first in adj:
                adj[first] = [(second, weight)]
            else:
                adj[first].append((second, weight)) 
        
        dists = {}
        dists[k] = 0
        completed = set()
        myq = [(0,k)]
        while len(completed) < n and myq:
            print(dists, completed, myq)
            currdist, node = heapq.heappop(myq)
            completed.add(node)
            for neighbor, weight in adj.get(node, []):
                if neighbor in completed:
                    continue

                if not neighbor in dists or weight + currdist < dists[neighbor]:
                    dists[neighbor] = weight + currdist
                    heapq.heappush(myq, (dists[neighbor], neighbor))
                
        if(len(dists)) != n:
            return -1 
        

        for val in dists:
            return max(dists.values())
                
                
                

            






        