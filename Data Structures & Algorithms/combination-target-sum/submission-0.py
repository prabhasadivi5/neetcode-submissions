class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #want to build up to approach the target
        #this seems liek a simple backtracking approach. 
        #since its all numbers and not shortest approach, we know its not dp 
        #combinations means order does not matter
        #so at each coin, we have the option to use the coin or move to the next one and use another coin
        #if the sum of the coin we use + the option, we add that to the final array
        #want to use copy(arr) or something alongthe lines of that, since arrays immutable and itll just make a pointer to it

        #1)create a function recurse that inputs the idx of the coin array and the prev sum
        #2)we can have a base case where if prevSum is greater, we return
        #3)Base case where if we have prevSum = to total sum, we add the array
        #4)Now for the recursive cases -> run recurse(sum+ curr, idx)
        #5) then after the recursive case remove from array
        #6) run recursive case recurse(sum, idx + 1) -> this will be nested in a forloop 
        #7)return 
        #8) outside of recurse have the array


        ret = []

        def recurse(prevArray, prevSum, idx):
            if prevSum > target: 
                return 

            if prevSum == target:
                finalizedArr = prevArray[::]
                ret.append(finalizedArr)
                return 
            

            prevArray.append(nums[idx])
            recurse(prevArray, prevSum + nums[idx], idx)
            prevArray.pop()

            if idx < len(nums) - 1:
                recurse(prevArray, prevSum, idx + 1)
        
        recurse([], 0, 0)
        return ret
