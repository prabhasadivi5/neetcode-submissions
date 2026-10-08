class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #given an numbers is sorted in increasing number
        #return the indeces such that they add up to target and index 1 < index 2
        #binary search with two pointers stands out to me
        #easily can be done in o(n) time with two pointers, go down 
        #maybe we can binary search?. we have left, right, and middleidx. 
        #if sum of left + r
        #its hard to binary search with two pointers though. 

        left = 0
        right = len(numbers) - 1


        while left <= right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] > target:
                right -= 1
            
            else:
                left += 1
        
        return [0,0]

