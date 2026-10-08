class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #return true if s can be segmented into a space segmented sequence of dictionary words.
        #the word dictionary is same scale as word size. 
        #lets start basic. We can iterate through the string and see if its in the dictionary. The actual word itself doesnt matter, just where the first break is. 
        #if no breaks obviously not there. If there is a break, we can just solve the same problem again. if there is no break, we go to the next index.
        #Potential complexity. if we have a dictionary where every index is a break -> we have to choose whether or not to use a break (2^n)
        #up to 20 chars

        #wordbreak[3,''] = wordbreak[4, fullstr] or wordbreak[4] if up to whatever we have is a string
        #up to a table where the x can be the index and the y is the string
        #if we are trying to find at index 4, we only need whatever is at index 3 and the any string and vice versa
        #the only true values-> wordbreak[length + 1, '']
        #if we want to buildup -> wordbreak[[4, str]] = wordbreak[3 + based on conditions]

        #up to length 20

        
        #create the 2d array where we have the size/substr of the word. We start at 0,0

        visitable = [False] * (len(s) + 1)
        nextvisitable = visitable[::]
        visitable[0] = True
        

        #i is the index of the string were at 
        #j is the index of the index of the prev string length were at  so visitable[i][j] means we are able to visit index i with a string of length j 
        for i in range(len(s)):
            for j in range(len(visitable)):
                if visitable[j]:
                    if j <= 20:
                        nextvisitable[j + 1] = True
                    if j <= 20 and s[i-j:i+1] in wordDict:
                        nextvisitable[0] = True
            visitable = nextvisitable
            nextvisitable =  [False] * (len(s) + 1)
        return visitable[0] 

                
                # i = 0, j = 0 
                # True False False False 
                # i = 1 j = 1 
                # False False TrueFalse 
                # i = 2 j = 2
                # False False False True
                # [i-j:i]
                # i = 1, j = 1 False False True False False False False
                
                # i = 2
                # False False False True False False False

                # c a t sin



                    
