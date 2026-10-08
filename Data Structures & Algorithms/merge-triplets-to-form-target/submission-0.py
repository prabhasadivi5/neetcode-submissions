class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #given an array of integers [x,y,x] which is the triplet we want
        #to get this triplet, we may just update triplet i and j to be maxes
        #to convert the array, we need 1) the target to be the bigger one of the two triplets AND 2) when doing merging/checking for the other 2, the max of whatever we have doesnt ruin what we already have
        

        #.  [[5,5,6],[1,4,4],[5,7,5]], [5,4,6]

        #to guarantee  a takeover of the second index while keeping first 
        #we can have the first index of the next one be less than equal to what we have and the second one be less than what we have
        #what if we set everything to the max first 
        #1) no matter what, we need an array with everything less than or equal to the target to take over the target
        #2)we can just do all our operations on this. We find all of the ones with 5, (max o(n)), then all of the ones with 4, then all of the ones with 6. The ones with 5 is worthless if the other two are greater than the boundary because we can never use it to create
        #)we can iterate through and check if we have 3 conditions -> 1 -> first with other 2 less than or equal to the target
        # second with other 2 less than or equal to target
        #third .. 
        #keep a track which ones have been satisfied. 

        firstPossible = False
        secondPossible = False
        thirdPossible = False

        for i in triplets:
            for j, val in enumerate(i):
                if j == 0:
                    if firstPossible or val != target[0]:
                        continue
                    if i[1] <= target[1] and i[2] <= target[2]:
                        firstPossible = True
                
                if j == 1:
                    if secondPossible or val != target[1]:
                        continue
                    if i[0] <= target[0] and i[2] <= target[2]:
                        secondPossible = True
                if j == 2:
                    if thirdPossible or val != target[2]:
                        continue
                    if i[0] <= target[0] and i[1] <= target[1]:
                        thirdPossible = True
        return firstPossible and secondPossible and thirdPossible
                        
                    