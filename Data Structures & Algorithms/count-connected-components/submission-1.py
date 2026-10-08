class disjointSet:
    def __init__ (self, n):
        self.parentList = [1]* n
        for i in range(n):
            self.parentList[i] = i
        self.size = [1] * n
    
    def find(self, n):
        if(self.parentList[n] == n):
            return n 
        else:
            return self.find(self.parentList[n])
    def union(self, u, v):
        uroot = self.find(u)
        vroot = self.find(v)
        if uroot == vroot: 
            return False
        
        bigroot, smallroot = 0,0
        if self.size[uroot] > self.size[vroot]:
            bigroot, smallroot = uroot, vroot
        else:
            bigroot, smallroot = vroot, uroot
        
        self.parentList[smallroot] = bigroot
        self.size[bigroot] += self.size[smallroot]
        return True 





class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mySet = disjointSet(n)
        totalSets = n
        for u,v in edges: 
            if mySet.union(u,v):
                totalSets -= 1
        return totalSets
            





