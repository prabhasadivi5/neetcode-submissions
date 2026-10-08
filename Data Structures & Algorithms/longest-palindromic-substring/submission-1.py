class Solution:
    def longestPalindrome(self, s: str) -> str:
        #substring reads the same forwards and backwards
        #if there are multiple, return one of them. 
        #can count longest palindromic substring starting from every index. 
        #have to account for both odd and even. 
        #We for odd, we can assume that we use the left
        #we need a way to store the longest substring. 
        #we can just store max length outside, and if the length of the substring we have is longer, we update


        # ababd

        #function that takes in the index, the lefternmost and rightmost (same if odd palindrome)
        #if no left/right or no right, dont match -> end the palindromic sequence
        #otherwise, we can pass into the input and update the longest sequence right there. Or, we can just say 2 + function call and then after the recursive call, we can do the checks. The issue with this is we will have to pass back both the string and the size. Or, for both function calls, we can pass back both strings and then just return. Otherwise, we keep the input string and return back 
        #once we are out, if the length of the new string is higher, we go next

        #1) setup loop with all starting indexes
        #2) for all indexes, we pass in string, left, right. If we want to be even more exact, we can just pass indexes, calculate index size, then just do substring -> better so we dont have to iterate to calc length
        #then iterate through the string, if index exists, we keep going until  + 1 right -1 left until they dont match or out of bounds. Then, we get we get the longest size and the longest index.
        #The runtime for this is o(n^2)
        #we each mini substring iteration starting at an index has up to 2*n calls and we have n centers
        #space is just o(1) storing few variables at once

        maxLen = 0
        currLeft = 0
        currRight = 0

        for i in range(0, len(s)):
            #one case
            leftidx = i
            rightidx = i

            while leftidx > 0 and rightidx < len(s) - 1 and s[leftidx-1] == s[rightidx+1]:
                leftidx -=1
                rightidx += 1
            
            if rightidx-leftidx + 1 > maxLen:
                currLeft = leftidx
                currRight = rightidx
                maxLen = currRight-currLeft

            #two case 
            if i < len(s) - 1 and s[i] == s[i+1]:
                leftidx = i
                rightidx = i + 1
            
                while leftidx > 0 and rightidx < len(s) - 1 and s[leftidx - 1] == s[rightidx + 1]:
                    leftidx -=1
                    rightidx += 1
                
                if rightidx-leftidx + 1 > maxLen:
                    currLeft = leftidx
                    currRight = rightidx
                    maxLen = currRight-currLeft

        return s[currLeft:currRight + 1]



