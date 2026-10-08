class Solution:
    def rob(self, nums: List[int]) -> int:
        #array where nums[i] is the amount of money the ith house has
        #the houses are in a straight line, the ith house is neighbors
        #cannot rob two adjacent houses
        #the system will alert the police if two houses were broken into 
        #questions: can we skip more than two houses? -> doesnt make sense anyways because might as well rob the middle one
        #break this into subproblems. At each house, the maximum we can get is either the value of the house right before or two houses before + the current house bring robbed
        # [2,9,8,3,6]
        # [2,9, 10, 12,  16]
        twoaway = 0
        oneaway = 0
        for i in range(0, len(nums)):
            currMax = max(twoaway + nums[i], oneaway)
            twoaway = oneaway 
            oneaway = currMax
        
        return oneaway