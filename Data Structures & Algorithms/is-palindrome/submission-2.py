class Solution:
    def isPalindrome(self, s: str) -> bool:
        #start on outside index
        left = 0
        right = len(s) - 1
        while left < right:
            leftval = s[left].lower()
            rightval = s[right].lower()

            if not ('a' <= leftval <= 'z' or '0' <= leftval <='9'):
                left += 1 
                continue
            if not ('a' <= rightval <= 'z' or '0' <= rightval <='9'):
                right -= 1 
                continue
            if leftval != rightval:
                return False
            left += 1
            right -= 1
        return True
        