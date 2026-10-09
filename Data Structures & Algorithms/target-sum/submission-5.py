class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
      #see how many ways we can add or subtract a number to get to the target sum. 
      #number of different ways we can build the expression such that the sum equals to the target
      #we can maybe use 2d dp? we can keep track of the numbers we already used while also tracking the number of ways we can get from there to the target
      #







    

    #number of ways we can reach each number given 1 
    #number of ways we can reach each number given 1,2 
    #number of ways we can reach each number given 1,2,3
    #number of ways we can reach each number given 1,2,3,4
    #we can keep an array of numbers sum(numbers), -1sum of numbers and iterate through it. 
    #this might be too slow because if a number is not visited, we will be slow. 
    #maybe keep a set and a dictionary. 
    #set of numbers we visited. 
    #if we havent visited it yet, we take that number and its negative. 
    #otherwise, we add to the visited set. We also add to the 0 


        reachableDict = defaultdict(int)
        reachableCopy = reachableDict.copy()

        for number in nums:
            if not reachableDict:
                reachableCopy[number] += 1
                reachableCopy[-1 * number] += 1
            else:
                for key, val in reachableDict.items():
                    reachableCopy[key + number] += val
                    reachableCopy[key - number]  += val
            
            
            
            reachableDict = reachableCopy.copy()
            reachableCopy = defaultdict(int)
        
        numreachable = reachableDict[target]
        return numreachable 

