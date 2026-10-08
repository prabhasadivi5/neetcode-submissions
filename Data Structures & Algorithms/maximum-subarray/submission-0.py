class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #maximum Subarray with the largest sum and return the sum
        #a subarray is a sum of elements within the array
        #nums = [2,-3,4,-2,  2,   1,-1,4]output = 8 
        # at position 2, if we have the max subarray sum of everything on the left and the max running sum, we can calculate it. So mSA(2) = max(sum(prev) + max(nearest)). Then, we also have to track the prev sum, overallmax. Then, we can keep going thru the array
        #so, if we use the runningmax and this is greater than the currmax, currmax = runningmax and then the runningmax just keeps growing
        #if we dont use the runningmax and use the currmax, we can say that the runningmax is the max of our curr value and currval + runningmax
        #first, we calculate the new runningmax
        #then if runningmax > currmax, currmax = runningmax else we keep going

        currmax = nums[0]
        runningmax = nums[0]
        for i in range(1, len(nums)):
            runningmax = max(nums[i], nums[i] + runningmax)
            if runningmax > currmax:
                currmax = runningmax
        return currmax
        