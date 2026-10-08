class Solution:
    def findMin(self, nums: List[int]) -> int:
        #array of length n originally in ascending order
        #now rotated n times 
        #a solution in o(n)logn
        #its a binary search with something around a pivot point. I think best way is to run through an example to see how the pivot works
        #[.6, 3,4,5,6, 1,2, 3.5, 3.75,]
        #first idea is to find the pivot (should take o(logn time))
        #the properties of the pivot: the left is less and the right is less
        #or even better we can find the min value -> if both the left and right are greater. 
        #if the left is less and the right is greater, its on the right
        #if the side is properly sorted(if on left and less or right and greater), pivot not on that side
        #we go until we get there
        #only worry is no (n) rations, then its just the first idx and no pivot error, end edge case

        #[4,5, 6,7, 1,2,3]
        #if right is greater than, we CAN have the middle, but if left is less than, mid cannot be(since we already have at least one less than)
        #if right greater and left less, we are at the pivot
        [3,4,  5, 6,1,2]
        left = 0
        right = len(nums)-1
        mid = (left + right) // 2
        while nums[right] < nums[mid] or nums[left] > nums[mid]:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1 
            else:
                right = mid
        
        return nums[left] 
            

            
           
        

        
        

        