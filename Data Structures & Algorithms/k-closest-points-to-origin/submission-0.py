import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #iterate throgh points, compute distance add to a heap. 
        #then just heappop them
        
        dists = []
        for x,y in points:
            dist = (math.sqrt((x)**2 +(y)**2))
            dists.append((dist, x, y))
        heapq.heapify(dists)
        kclosest = []
        for i in range(k):
            dist, x, y = heapq.heappop(dists)
            kclosest.append([x,y])
        return kclosest


        