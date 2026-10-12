#heights[i] -> height of the ith bar

#can choose any two bars to form a container. Return the maximum amount of wter a container can store. 

#the amount of water is -> the minimum of the two heights times the distance 

#the first appraoch I have -> quote on quote naive is o(n^2) where we check every starting index, if a bar in between the starting and end is greater, then the end is the greatest.


#[1,7,2,5,8,7000,800000,6]
#7, 800000  
#if left is limiting factor, we can obviously keep searching to the right
#if a value is greater than the left ptr but less than the right ptr -> we can chooise whether we move left or right based on which one is bigger. If a value is less than both, we can move only right (since the new value is the limiting factor anyways)
#if left is bigger, we move anyways right only since the right is the limiting factor and moving left makes smaller
#if the right is bigger, we have more cases. We can either expand only the right, or expand right and left. Or we can take the max value 
#if left is smaller, we can keep moving the left until the calculation is bigger than moving it one over
#we find the left with the maximum value (added to right, we want the maximum up to that index.) 

#what if we start in the middle. We only move the limiting factor to the right one (even if its smaller)
#Store the max. This should work because 
#what if we start one on the left and right. Two pointer approach. Since The bucket is only as big as the smallest bar, we move the smaller bar in. 
#if the new max is greater, good. Otherwise, we keep going 
#4 cases: 1) value on the right greater than both 2) greater than left not right 3) greater than right not left 4)smaller than both. 

#see if the left or right pointer is greater. If the right pointer is greater, 
#maybe we can take a running max based on the left and right pointer. 

#   a   b

#want to know when we can/need to move the left ptr. 
#1
#what if we use two pointers and iterate through? 
#store the max though, because the size of the bar can vary. 
#Why does this work? The outsides will always be greater than the inside (7-4 always greater than 7-5 (not true))
#if the volume could possibly be greater(new bar is less)

#if its a tie what do we do?
#first idea is to find the one next to them and move the one with the smaller neighbor

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftptr = 0
        rightptr = len(heights) - 1
        maxarea = 0
        while leftptr < rightptr:
            leftheight = heights[leftptr]
            rightheight = heights[rightptr] 
            maxarea = max(maxarea, ((rightptr-leftptr)* min(leftheight, rightheight)))

            # if leftheight == rightheight:
            #     if leftptr == rightptr - 1:
            #         break
            #     elif heights[leftptr + 1] > heights[rightptr - 1]:
            #         leftptr += 1
            #         continue
            #     else:
            #         rightptr -= 1
            # else:
            if leftheight > rightheight:
                rightptr -= 1
            else:
                leftptr += 1
        return maxarea

        