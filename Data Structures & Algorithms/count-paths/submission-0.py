class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #we want to calculate the number of unique paths given m and n
        #we should cache each, so then if we come to a path we already know
        #so for the recursive equation, we know that the one directly to the right and left is 1
        #we also know that the 
        #UP(m-2)(n-1) = 1, UP(m-1)(n-2) = 1
        #From here, we know UP(m)(n) = UP(m+1)(n) + UP(n)(m+1) -> we also know that if m and n dont exist, (out of grid, we dont add) -> so we have the edge cases too
        #we actually dont even need the base case, since we know dp mn is 1

        dp = [0] * m
        for i in range(len(dp)):
            dp[i] = [0] * n
        
        dp[m-1][n-1] = 1

        for midx in range(m-1, -1, -1):
            for nidx in range(n-1, -1, -1):
                if midx == m-1 and nidx == n-1:
                    continue
                elif midx == m-1: 
                    dp[midx][nidx] = dp[midx][nidx+1]
                elif nidx == n-1:
                    dp[midx][nidx] = dp[midx+1][nidx]
                else:
                    dp[midx][nidx] = dp[midx+1][nidx] + dp[midx][nidx+1]
        return dp[0][0]
        
