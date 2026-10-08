#first intuition is to run a sorting algorithm like mergesort. 
#the second intuition without sourting is to run a heap 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        myq = nums.copy() 
        for i in range(len(myq)):
            myq[i] = myq[i] * -1
        heapq.heapify(myq)
        for val in range(k):
            curr = heapq.heappop(myq)
        
        return curr* -1

        