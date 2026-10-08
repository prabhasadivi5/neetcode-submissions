class Solution:

    def __init__(self):
        self.stringToArrayDict = defaultdict(list)

    def encode(self, strs: List[str]) -> str:
        ret = ''
        for val in strs:
            ret += val
        self.stringToArrayDict[ret] = strs
        return ret

    def decode(self, s: str) -> List[str]:
        return self.stringToArrayDict[s]



    #algorithm to encode a list of strings into a string
    #then, the string is sent over the network and decoded back to the original list of strings
    #So far, this seems simple -> all we need to do after a decode is to store the indices/lengths of the strings in the class
    #then, when decoding, decode based on this. 
    #so we can have a dictionary from a string to anything like an array, another dictionary
    #an array is easy, so we can just iterate through it. 
    #in the array, we store the length of each string
    #class has the dict to array 
    #encode we create the array and then put the index array in the dictionary 
    #we can also just put a copy of the array into a dictionary -> might be a little slower
    #then we can just return the dictionary value 