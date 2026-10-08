class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #the length of the longest consecutive sequence of elements that can be formed
        # Input: nums = [2,20,  4, 10,3,4,5] 
        # lcs at 4 is just 1 + max LCS of everything before it thats less than 4. This would be o(n^2) since we have to check if anything below 4 and iterate everything else
        #what is we track the min, max of each subsequence in a dictionary maybe? 
        #and then if the number we have is in that sequence, we can add to the min and max
        #keep a dictionary with both the min and max of a sequence
        #so if the min is 2 and the max is 3, they both point to the array [2,3] -> can be different ones
        #then, we know the biggest and smallest one. if its 1 below the biggest and 1 above the smallest (connecting, then we just connect the intervals)
        #if its one below, we move the smallest and also edit the interval in the big side
        #if its one above, we move the biggest and edit the interval in the small side
        #otherwise, we add to the new dict
        used = set()
        maxdist = 0
        intervalsDict = defaultdict(tuple)
        for num in nums:
            if num in used:
                continue
            used.add(num)
            if num + 1 in intervalsDict and num - 1 in intervalsDict:
                
                smallend = intervalsDict[num - 1][0]
                bigend = intervalsDict[num+1][1]

                if intervalsDict[num-1][1] != smallend:
                    intervalsDict.pop(num -1)
                    
                if intervalsDict[num+1][0] != bigend:
                    intervalsDict.pop(num + 1)

                intervalsDict[smallend] = (smallend, bigend)
                intervalsDict[bigend] = (smallend, bigend)

         

                if bigend-smallend + 1 > maxdist: 
                    maxdist = bigend-smallend + 1

            elif num + 1 in intervalsDict:
                rightval = intervalsDict[num+1][1]
                if num + 1 != rightval:
                    intervalsDict.pop(num + 1)
                
                intervalsDict[num] = (num, rightval)
                intervalsDict[rightval] = (num, rightval)


                maxdist = max(rightval - num + 1, maxdist)
            elif num - 1 in intervalsDict:
                leftval = intervalsDict[num-1][0]
                if num - 1 != leftval:
                    intervalsDict.pop(num-1)
                
                intervalsDict[num] = (leftval, num)
                intervalsDict[leftval] = (leftval, num)
                

                maxdist = max(num - leftval + 1, maxdist)
            else:
                intervalsDict[num] = (num, num)
                maxdist = max(1, maxdist)

        return maxdist

