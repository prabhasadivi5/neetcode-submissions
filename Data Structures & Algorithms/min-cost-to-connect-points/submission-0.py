import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #kruskals algorithm 
        #initial thought is to first calculate the distances between EVERY point, since thats an option
        #then we sort by smallest distance
        #then we compute

        #issue is we dont need to calculate distances for points we already have
        #calculate all distances from our starting point
        #then find the shortest, add to MST. Then, we calculate all distances from our two points -> either way we have to calculate the mins of all to get it in
        #keep a set to track already visited
        #if already visited, we can pop
        #prims algorithm is optimal here
        #start with a node
        #have a heap/sorted list of elements connecting not in to inside. if we do use it, we pop. 

        #1) start at a point
        #2) compute the distance from that point to every other point, put it into a heap
        #3) the smallest of the heap gets taken out, that new point added to visited group
        #4) now, that new point, take all the points (except the visited) and add to the heap
        #5) now keep doing with all new points, we can keep a set of connections so we know which connections not to calculate and add to the heap


        currpoint = points[0]
        xval, yval = currpoint
        visitedpts = set()
        visitedpts.add((xval, yval))
        totalcost = 0
        priorityqueue = []
        xval, yval = currpoint
        while(len(visitedpts) < len(points)):
            
            for visiting in points:
                newx, newy = visiting
                if (newx, newy) in visitedpts:
                    continue
                
                heapq.heappush(priorityqueue, (abs(xval-newx) + abs(yval - newy), newx, newy))

            smallestdist, xval, yval = heapq.heappop(priorityqueue)
            while (xval, yval) in visitedpts:
                smallestdist, xval, yval = heapq.heappop(priorityqueue)
            totalcost += smallestdist
            visitedpts.add((xval, yval))
        return totalcost

            
            





        