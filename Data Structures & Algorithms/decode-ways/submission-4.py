class Solution:
    def numDecodings(self, s: str) -> int:
        #we will get a letter and that decodes to a string.
        #to decode a string, there are multiple ways we can do it based on teh digits
        #this is pretty simple dynamic programming. 
        #the first approach would be to just do it recursively. If we see a two or a 1, we check if there is 1-6, and if there is, we call recursively on that with a + 1 in the front to return the sum. However by tracking states, we can remove redundancy.
        #at any given index, we can calculate the number of ways from the front by doing two things:
        #if the number is a 1 or 2 abd tgere exusts bext bnum + its 0-6, then we have two things to check. DP[i] = DP[i+1] + DP[i + 2] we already have one way to decode(since its default), so just add one. 
        #we know that DP[len(s-1)] = 1 and DP[s-1] is 1 or 2 depending on whatever it may be.
        #if the number cannot be decoded, it returns zero(if the number first is a zero) or the number next is 

        #1) base cases -> array longer and then just set the vals to zero. 
        #2) setup the loop backwards
        #3) set cases -> if val 1 or 2 and next 0-6 its both, otherwise its only the one after
        #4)update i+1, i+2
        #5) return DP[0]
    
        #if we get a number like 101


        if len(s) == 1:
            if s[0] != '0':
                return 1
            return 0 

        oneaway = 1
        twoaway = 1
         

        for i in range(len(s) - 1, -1, -1):
            curr = 0
            if i < len(s) - 1 and  s[i] == '1' and '0' <= s[i+1] <= '9':
                curr = oneaway + twoaway
                
            elif i < len(s) - 1 and s[i] == '2' and '0' <= s[i+1] <= '6':
                curr = oneaway + twoaway

            elif s[i] == 0 :
                curr = 0
            
            elif '1' <= s[i] <= '9':
                curr = oneaway
            
            twoaway = oneaway
            oneaway = curr
        return oneaway

                

