class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = defaultdict(int)
        tDict = defaultdict(int)
        for val in s:
            sDict[val] += 1
        for val in t:
            tDict[val] += 1
        
        return sDict == tDict
        