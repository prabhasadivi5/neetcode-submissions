class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        #all combinations
        #return all well formed pairs of parenthesis 
        #we want the left to equal to right to return, and we keep going 
        #if the # of pairs = n -> only if its closed, then we return back out 
        #otherwise, we keep going 
        #on each iteration, we have to track, opened, closed, and pairs
        #1)check if open == closed, if so, we add to ret
        #2)next we check if we are at open = closed = n, if so we return 
        #3)now we do our backtracking algorithm. If open > closed, we have the ability to open
        #4)if open < n, we have the ability to add open

        def recurse(opened, closed, currStr):
            if opened == closed == n:
                ret.append(currStr)
                return 
            
            if opened > closed:
                currStr += ')'
                recurse(opened, closed + 1, currStr)
                currStr = currStr[0:len(currStr)-1]
            
            if opened < n: 
                currStr += '('
                recurse(opened + 1, closed, currStr)
                currStr = currStr[0:len(currStr)-1]
        
        recurse(0,0, "")
        return ret

        