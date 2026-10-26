class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #see if we can reach the last index starting at zero 
        #work backwards, see if we can reach the end
        #the first idea is to simply work backwards, see if its reachable, mark it, and if not, its not reachable. 
        #the issue is that each index, we have to check every index in front of it
        #one idea is to use a set of visitable, then add from the jump value
        #o(1) space
        #what if we just track max jump space at any index
        #so at the beginning, its one
        #then, at the next index its max(1-1, 2).
        #keep going until we at the end or fail

       # Input: nums = [1,2,1,0,1]

        if len(nums) == 1:
            return True

        # [1,2,0,1,0]
        jumpsleft = 0
        for i in range(0, len(nums) - 1):
            currjumps = max(jumpsleft - 1, nums[i])
            if currjumps <= 0:
                return False
            jumpsleft = currjumps
        return True 
            

        