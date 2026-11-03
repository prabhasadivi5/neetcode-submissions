
from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
       

        tasksDict = defaultdict(int)
        for curr in tasks:
            tasksDict[curr] += 1
        
        myheap = []
        for key, val in tasksDict.items():
            myheap.append((-1*val, key))
        
        heapq.heapify(myheap)

        waitinglist = deque()
        time = 0


        #currtime - totaltime 
        while waitinglist or myheap:
            if myheap:
                topfreq, topval = heapq.heappop(myheap)
                if topfreq < -1:
                    waitinglist.append((topfreq + 1, topval, time))
            else:
                time = waitinglist[0][2] + n
            
            while waitinglist and time - waitinglist[0][2]  >= n:
                currfreq, currval, currtime = waitinglist.popleft()
                heapq.heappush(myheap, (currfreq, currval))
            time += 1
        return time
                

       
        
                

        