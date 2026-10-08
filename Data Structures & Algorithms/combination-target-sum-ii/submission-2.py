class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #all unique combinations that sum to target. Each element may be chosen at most once within a combination, no duplicate combinations
        #Since its all unique combinations the first thought is backtracking
        #we can just prevent duplicates by first sorting and if the prev is the same as the current, we dont use (since we already had the opportunity to use multiples in the prev iteration)
        #we iterate through every index, have two cases : use and dont use. 
        #if we use the previous character and the curr is the same, we choose both options. 
        #if we dont use the previous character, we dont use the current one if its the same. 
        #maybe store a past uswed variable?


        #.   [9,2,2,4,6,1,5] 
        
       # [1,2,2,3,4,5,6,9]
        #in each recursive call, we need the currSum, the index, and the currArray as well as if we used the prev (only matters if its the same)

        #define ret
        #define the recurse function
        #make sure to bacltrack after each function call
        #we dont need to return anything. just append to ret as we go 
        #call recurse o teh fist number


        ret = []

        candidates.sort()
        def recurse(index, currSum, currArray, prevUsed):

            if index > len(candidates) - 1:
                return 
                 
            if currSum + candidates[index] > target:
                return 
            
            if currSum + candidates[index] == target:
                currArray.append(candidates[index])
                ret.append(currArray[::])
                currArray.pop()
                return
            
            
            if not (index != 0 and prevUsed == False and candidates[index] == candidates[index-1]):
                currArray.append(candidates[index])
                recurse(index + 1, currSum + candidates[index], currArray, True)
                currArray.pop()

            recurse(index + 1, currSum, currArray, False)

        recurse(0, 0, [], False)
        return ret
            
            

                


        