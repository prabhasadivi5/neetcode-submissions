class Solution:
    def canPartition(self, nums: List[int]) -> bool:
       #return True if you can partition the array into two subsets
       #otherwise return False
       #instantly, we think greedy where we sort and then add the biggest and the smallest. If the biggest + smallest is greater, do smallest + second biggest.
       #the issue is that if we are less than, we have to decide between adding and making less, which can cause o(n)^2
       #maybe a dynamic programming approach. We have a target of sum(nums)/2 since thats half of it. 
       #at any given point, we need to keep track of the numbers used and whether its possible or not
       #so we can theoretically start with a 2d array
       #the bottom will get filled as true/false and the top whether a number has been used or not so its an nxn array

       #ex, if we have a target of 10 and have 1,2,5
       #in the bottom, 8, 9, 5 will be marked as visitable -> this solution is slow as its n^3. We need a set within each to see whether ti was used or not. 
       #What if we build backwards?
       #we start at 10. We then know we can reach 5. We put 10 in the used set. 
       #we only need to know the numbers used and whether the solution is reachable at a certain point. 
       #so, we can start either way. 
        target = sum(nums)/2
        reachable = set()
        temp = set()
        reachable.add(0)
        for num in nums:
            reachable = reachable | temp
            for currval in reachable:
                if currval + num not in reachable:
                    temp.add(currval + num)
            if target in reachable:
                return True
        return False

        