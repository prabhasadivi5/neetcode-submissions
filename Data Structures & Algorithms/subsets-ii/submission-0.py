class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #run through, if the prev is the same and its a 1, we have both, if its diff and its a zero, we keep 

        newnums = sorted(nums)

        ret = []
        def recurse(arr, idx, prev, used):
            #we have the array sorted
            #if the previous is the same value and we did not use it, then it MUST not be used
            #if the previous is different, then we have the option to choose
            #the zero case will always have the option, prev for the zero case can be outside the index
            #first zero and outside case

            if(idx == len(newnums)):
                return
            if(idx == 0):
                ret.append(arr.copy())
                recurse(arr.copy(), idx + 1, newnums[0], False)
                arr.append(newnums[0])
                ret.append(arr)
                recurse (arr.copy(), idx + 1, newnums[0], True)
            #case where previous is zero, so this must be zero
            elif(used == False and newnums[idx-1] == newnums[idx]):
                recurse(arr.copy(), idx + 1, newnums[idx], False)
            #normal case, we either use a number or we dont. 
            else:
                recurse(arr.copy(), idx + 1, newnums[idx], False)
                arr.append(newnums[idx])
                ret.append(arr)
                recurse(arr.copy(), idx + 1, newnums[idx], True)
        recurse([], 0, -21, False)
        return ret









        