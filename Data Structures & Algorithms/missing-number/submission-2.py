class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #return number that is missing from nums. 
        #the original solution is to use a set
        #but we cannot use space complexity. 
        #we must store inside the array. 
        #We can just mark each visited index as negative (include the nextIndex)
        #the array is one short because we are missing a value. We can just add n+1 and mark it negative
        tsum = sum(nums)
        expectedSum = ((len(nums) + 1)*len(nums))/2

        return int(expectedSum-tsum)


        