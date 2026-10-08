class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [1] * len(nums)
        for i in range(len(nums) -1, -1, -1):
            for j in range(i, len(nums)):
                if(1 + arr[j] > arr[i] and nums[j] > nums[i]):
                    arr[i] = 1 + arr[j]
        
        print(arr)
        

        return max(arr)
        