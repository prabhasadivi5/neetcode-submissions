from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #we can use djikstras to track the number of steps. 
        #we know that djikstras tracks the shortest path to a certain point. 
        #in the djikstras though, we also need to keep track of the number of steps 
        #if the #steps is greater and the path to the node is longer anyways, we remove. 
        #if the number of steps exceeds k, we remove. 
        #otherwise, if its less than k and longer, we just add it to the queue. 
        #explore all of the shortest paths first, if it is greter than k remove, keep going 
        #whats the runtime for this? regular djikstras is o(v+e)log(v). But, we might have to add the same node up to k times since thats the dist. So, the runtime is o(k*logv*m)
        #what about bellman fords. we just run k iterations and store the min for every node. 
        #we know the min locked distance is the smallest one in the bellman ford algorithm
        #so we can either lock it or keep going. 
        #tracked locked nodes first idea is to use an array with a tuple. the first is the dist, the second is if its completed. 
        #this doesnt work for negative nodes, but for positive nodes we can do this
        #if the array of the val is true -> return that val 
        #if not, we keep going until we run k times or not

        adjacency = defaultdict(list)
        for newsrc, dest, price in flights:
            adjacency[newsrc].append((dest, price))

        #poplate the array
        distances = [(99999999999)] * n
        distances[src] = 0
        nextdistances = distances.copy()
        #now, we need a bfs, and the smallest in each bfs gets marked small. If distances(dest) == True or we hit k, we can escape 
        #am realizing to calculate the min val, we either have to calculate it while populating it. track mindex and minval. But the issue is each search is o(n). instead of multiplying by n times, we can just go k times

        myq = deque()
        myq.append(src)
        currk = 0
        while myq and currk < k + 1: 
            for _ in range(len(myq)):
                curr = myq.popleft()
                for destination, price in adjacency[curr]:
                    if distances[curr] + price < nextdistances[destination]:
                        nextdistances[destination] = price + distances[curr]
                        myq.append(destination)
            distances = nextdistances[::]
            currk += 1

        
        if distances[dst] == 99999999999:
            return -1 
        return distances[dst]








        
        
        