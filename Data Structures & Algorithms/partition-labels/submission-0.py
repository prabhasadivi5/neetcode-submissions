class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #a string consisting of lowercase english letters
        #split into as many substrings as possible, ensuring each letter in at most one substring
        #return a list of integers representing the size of these sustrings in the order they appear int he string. 
        # "xyxxy zbz bb i s l"
        #the trick for this is clearly that we have to see where the first and last index of each x and y is. 
        #we could easily do this in two iterations. 
        #find the last occurence each letter. 
        #then, start at the beginning. if we are at the letter and the index is the last index, the max index is the last index
        #everything inside it has to be in one substring no matter what. The thing is the max index could be EXPANDED if something inside it expands after. 
        #so we track currmax. If currmax is the last num, we are done. Otherwise, we get to the maxindex cleanly and end

        #1) populate the dict with the last index
        #2) start with lastidx = 0, then start iterating through the array
        #3) when iterating, if i == maxidx, add currsize to the return array, set currsize to 0 and start over at the next idx
        #4) if maxidx == len(str) - 1, then add len(str) - 1 + currsize - i (check for one off errors) and return 
        mydict = defaultdict(int)
        for i, val in enumerate(s):
            mydict[val] = i
        
        currsize = 0
        currmax = 0
        ret = []
        for i, val in enumerate(s):
            currsize += 1
            currmax = max(mydict[val], currmax)
            print(currmax)
            if currmax == len(s) - 1:
                ret.append(len(s) - i + currsize - 1)
                return ret
            if i == currmax:
                ret.append(currsize)
                currsize = 0
                continue
            
        return ret