from collections import defaultdict 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #first we have a dictionary for the number of everything in s2 -> numbers of abcdef ... etc. 
        #this is o(n)
        #then, we have another dictionary for the number in everything in the first window in s1. 
        #we iterate through this and see how many are equal -> we want the number of equals to be the size of the dictionary of s2
        #then, we slide the window. we remove the left one and add the new right character. If the right character makes a new equal, we add matches plus 1. we then check if the left removes an equal and then if it does matches -= 1. We go unitl we have the equal matches, if its true done return true
        #keep going return false if we make it out

        #0)edge case -> if s1 longer than s2, we obviouslt have an issue, return false
        #1)populate the dictionary for s1, find the length of s1 dict and call it matchesNeeded
        #2)populate the windowdictionary with what we have. 
        #3) compute matches by comparing the dictionaries -> if s1dict[s1] <= windowdict[s2] -> the window needs to ahve more than s1. Then matches += 1
        #4) if matches < matchesneeded, iterate, otherwise return true
        #5)keep going until the last index

        #loop is starting at length s1, ends len(s2)
        
        #a1 b0 c1 l0 e0 c1


        #subtract the value from windows s2
        #say if value in s1 != 0 and windows[val] == s2dict[val] - 1 -> matches -= 1
        #if value in s1 != 0 and windows[val] == s2dict[val] -> matches += 1

        #keep going 
        #initial matches calc : if s1dict[val] != 0 (wont be we populated) and window[val] >= s1dict[val] -> add 1 

      #matches = 1

            
       # s1 = "abc", s2 = "leca bee "
        if len(s1) > len(s2):
            return False
        

        s1ValsDict = defaultdict(int)
        windowValsDict = defaultdict(int)

        for val in s1:
            s1ValsDict[val] += 1
        
        for i in range(len(s1)):
            windowValsDict[s2[i]] += 1
                
        matches = 0
        matchesTarget = len(s1ValsDict)
        for key,val in s1ValsDict.items():
            if windowValsDict[key] >= val:
                matches += 1
        
        if matches == matchesTarget:
            return True

        for i in range(len(s1), len(s2)):
            firstInWindow = s2[i-len(s1)]
            newInWindow = s2[i]

            windowValsDict[firstInWindow] -= 1
            if s1ValsDict[firstInWindow] == windowValsDict[firstInWindow] + 1:
                matches -= 1

            windowValsDict[newInWindow] += 1
            if s1ValsDict[newInWindow] == windowValsDict[newInWindow]:
                matches += 1
            if matches == matchesTarget:
                return True
        return False 


            