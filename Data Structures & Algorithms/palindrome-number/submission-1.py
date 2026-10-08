class Solution:
    def isPalindrome(self, x: int) -> bool:
        start = 0
        

        currstr = str(x)
        end = len(currstr) - 1
        
        while end > start:
            if currstr[start] != currstr[end]:
                return False
            end -=1
            start += 1
        return True
        