import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      #piles is the number of bananas at idx
      #h is the number of hours we have to eat all the bananas
      #we decide bananas per hour eating rate of k
      # each hour we chose a pile of bananas and eat k bananas from that pile. 
      #if it has less than k, we finish, but cannot eat from the same pile
      #Point of problem is min eating rate we can finish everything. The eating rate will be between 0 and k
      #so if we know the number of hours we have, we can work our way back based on teh array size. 
      #so first we sort, which is o(piles)log(piles)
      #we can also just binary search on h and if its less, we go higher and if more, we go lower
      #this is o(logh) * time it takes to calculate 

      #algorithm 
      #1) max right now would be the max of the array /len array. Since all this number is is the number of times we go through the array. 
      #2) calculate if we are able to eat or not. If we are not able, find the middle between current and max 
      #3) If we are able, go back down (this is if we are below h)
      #4) if the time taken our k == h, we still can go down
      #5) calculating the go down case: first idea is to still do binary search until left ptr == right ptr 
      #6) lets do in head 
        # piles = [1,2,3,4] h = 9

        # mid = 1
        #left = 1
        #right = 2
        #so we eat in 5, so the binary search goes up. We keep going until left == right. if l

        def calculateHours(k):
            tot = 0
            for pilesize in piles:
                tot += math.ceil(pilesize/k)
            return tot

        left = 1
        right = max(piles)
        mid = right//2
        while left != right:
            if h >= calculateHours(mid):
                right = mid
                mid = right //2
            else:
                left = mid + 1
                mid = (left + right) // 2
        return left 
            
        #because left fails, we have to make sure to exclude it




        



