class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #dictionary to track the frequency of each, so then we can add one to the frequency and then move it over one 
        mydict = {}
        freq = []
        for i in range(len(nums)+1) :
            freq.append(set())
        for i in range(len(nums)):
            if nums[i] in mydict:
                freq[mydict[nums[i]]].remove(nums[i])
                mydict[nums[i]] += 1

            else:
                mydict[nums[i]] = 1
        
            freq[mydict[nums[i]]].add(nums[i])

        ret = []
        for i in range(len(nums), -1, -1):
            if k == 0:
                return ret
            for val in freq[i]:
                if k >= 0:
                    ret.append(val)
                    k-=1
        return ret
            
        
        



