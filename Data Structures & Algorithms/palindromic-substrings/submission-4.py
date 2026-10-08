class Solution:
    def countSubstrings(self, s: str) -> int:
        #substrings within s that are palindromes
        #same forwards and backwards, includes one characters
        #the initial intuition is to start in the middle and then move to the right. 
        #the issue is could have either odd or even length on both sides.
        #first is start at len(str)//2
        #then, since we are already going to be right heavy no matter what, if its even, we will have the extra on the right.
        #if its odd, we will have on the left
        #Not true because the left 2 aa
        #what if we check for both. odd going both sides(if possible) and even with the one on the right being the middle pointer and then moving right until fail or exit 
        #start at index 0 at the center and keep going 
        #each individual is also there

        tot = 0

        def countPalindromes(left, right):
            intot = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                intot += 1
                left -= 1
                right += 1
            return intot

        for center in range(0, len(s)):
            #add for individual case 
            tot += 1 

            #even case
            left = center 
            right = center + 1
            if(right < len(s) and s[left] == s[right]):
                tot += 1
                tot += countPalindromes(left - 1,right + 1)
                
            #odd case 
            tot += countPalindromes(center - 1, center + 1)
        return tot
            

        
        
