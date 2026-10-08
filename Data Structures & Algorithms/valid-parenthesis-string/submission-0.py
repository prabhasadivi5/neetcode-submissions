class Solution:
    def checkValidString(self, s: str) -> bool:
        #a string is valid if each parenthesis has a valid left, riht, and we also have a star
        #so if we are at any index, left must be >= right
        #if we are at the end, left must be == right
        #so first idea is recursively, we go through it, consider both possibilities -> track idx, left, right if idx at end left == righjt, return true
        #we know that when we recurse, at each level, we might have the same number of lefts, rights and index. 
        #so, we can use a memoization table to track where we are, and if we are already in the table, we are good
        #The time complexity would be optimized here, since we are only calculating at max len(s) *len(s) possibilities. 
        #the storage is also this, since we calculate every combination of closed and open. 
        # we can optimize it even further by tracking only one row at a time. 
        #base case is open = closed , open + closed = len(s)
        #bottom down approach. 
        #we can first start at closed = n/2
        #idx = at the end. 
        #if we have the ability to close, then (open, closed-1) = stays the same
        #if we dont have the ability to close (its false) 
        #then, we can start at the second last row, open is one less. If adding a close returns true, then we can keep going.  

        #track open - closed 
        
        
        #this is where idx at the end and open - closed = 0
        #open - closed can be a max len(s)//2
        #now iterate through the number of closes. 
        #if the last one is a star, we use a close
        #if its a close, we use a close
        #if it is an open, we just set that to false
        
        
        #we are iterating from the back on the string, based on the number of closes
        # all we care about is idx and closed - open
        #so at the next one, we go back an index, and given closed-open
        #if its a star, we can check it 
        ret = [False] * ((len(s) // 2) + 1)
        ret[0] = True
        opendiff = 0
        nextret = ret[::]
        for curridx in range(len(s)-1, -1, -1):
            currval = s[curridx]
            for i in range(len(ret)):
                if currval == '*':
                    if i > 0 and i < len(ret) - 1:
                        nextret[i] = ret[i + 1]  or ret[i - 1] or ret[i]
                    elif i > 0:
                        nextret[i] = ret[i - 1] or ret[i]
                    elif i < len(ret) - 1:
                        nextret[i] = ret[i+1] or ret[i]
                    else: 
                        nextret[i] = ret[i]
                elif currval == ')' and i > 0 :  
                        nextret[i] = ret[i - 1]
                elif currval == '(' and i < len(ret) - 1:
                        nextret[i] = ret[i + 1]
                else:
                    nextret[i] = False
            ret = nextret[::]
        
        return nextret[0]

            
            


        