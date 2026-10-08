class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #each slot is the product of everything except it. 
        #first intuitive approach is to take the total product and then just divide it by the actual number 
        #now without the division operation is more tricky: we multiply everything except it thats o(n) ^2, so no way to do that. 
        #maybe theres a way to store it so that we dont multiply 
        #perfix suffix tech
        leftarr = []
        leftmult = 1
        for i in range(0, len(nums)):
            leftarr.append(leftmult)
            leftmult = leftmult*nums[i]
        
        rightarr = []
        rightmult = 1
        #start at the right end of the array. The first will be 1, and then the second will be 1* the next etc. The right array will be stored backwards, since thats the way its calculated, so when doing final calc takes more effort
        for i in range(len(nums) -1, -1, -1):
            rightarr.append(rightmult)
            rightmult = rightmult*nums[i]
        ret = []
        for i in range(len(nums)):
            ret.append(leftarr[i] * rightarr[len(nums)- 1 - i])

        return ret
        