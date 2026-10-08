class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        totmax = nums[0]
        currmax = nums[0]
        currmin = nums[0]
        for i in range(1, len(nums)):
            oldmax, oldmin = currmax, currmin
            currmax = max(nums[i], oldmax * nums[i], oldmin * nums[i])
            currmin = min(nums[i], oldmax * nums[i], oldmin * nums[i])
            totmax = max(totmax, currmax)
        return totmax