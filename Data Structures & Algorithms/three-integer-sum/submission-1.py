class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #return all the triplets where nums[i] + nums[j] + nums[k] == 0
        #no duplicates
        #the first idea is obviously to bruteforce each combination. This is o(n)^3.
        #then maybe do a sort on all 3 arrays then keep going. (worst case this is o(n^3) too still though)
        #keep 2sum in mind where we store every number in a set and if the curr num = num in set, we keep it. 
        #what if we do 2 sum but n times. 
        #so this is like the first array is in a set. 
        #then, the second array is also in a set
        #then, iterate through the third array -> issue is we dont know the conbinations, well have to iterate thru the second array anyways
        #we can do this in o(n)^2 easily though by using 2sum, iterating through every first and second combination and seeing if it is in the set
        #sort the array, start at the smallest and biggest indexes of
        # [-1,0,1,2,-1,-4]
        # [-4,  -1, -1, 0, 1, 2]
        ret = []
        for i, firstval in enumerate(nums):
            print(i)
            if i >= len(nums) - 2:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while r > l:
                if (l > i + 1 and (nums[l] == nums[l-1])):
                    l += 1
                    continue
                if (r < len(nums) - 1 and nums[r] == nums[r+1]):
                    r-=1 
                    continue

                if firstval + nums[l] + nums[r] == 0:
                    ret.append([firstval, nums[l], nums[r]])
                    r -= 1 
                    l += 1
                elif firstval + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return ret 
        
