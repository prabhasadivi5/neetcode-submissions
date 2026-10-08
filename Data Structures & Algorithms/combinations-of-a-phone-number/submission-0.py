class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        #all possible combinations 
        #so digits 2->9 have to go through each. 
        #the first Idea is to have a dictionary of arrays where we populate each
        #then, we run a backtracking algorithm for each
        #so the #123 for example 
        #we se 1, iterate through the dict array, try the 3 combinations, explore till the end, then backtrack. 
        #we have a recursive function, each input is idx #, prev string, and return 
        #we dont even need to backtrack, we can just have the # of calls 
        ret = []
        mydict = { '2' : ['a','b','c'], '3' : ['d' ,'e', 'f'], '4' : ['g' ,'h', 'i'], '5' : ['j' ,'k', 'l'], '6': ['m', 'n', 'o'], '7' : ['p', 'q', 'r', 's'], '8' : ['t', 'u', 'v'] , '9' : ['w', 'x', 'y', 'z']}
        def recurse(idx, prevStr):
            if idx == len(digits):
                ret.append(prevStr)
                return
            for digit in mydict[digits[idx]]:
                prevStr += digit
                recurse(idx+1, prevStr)
                prevStr = prevStr[0:len(prevStr)-1]
            return
        recurse(0, '')
        return ret



        