class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        grid = matrix
        myarr = []
        for i in range(len(grid)):
            copygrid = grid[i][::]
            myarr.append(copygrid)
        distGrid = myarr
        #2D grid of integers where each integer is greater or equal to zero
        #return the length of the longest STRICTLY increasing path within matrix
        #First solve longest increasing substring. We can 
        #to find the longest increasing substring of the one leading up to our number, max length of substring with 
        #12345667
        #This would just be longest increasing substring within the grid?
        #Bruteforce is trying every combination. n^4
        #idea is to start at the top right, calculate down whatever is shorter. But, we can move wherever. We can visit each spot multiple times too 
        #So the DP has to be number of moves and the grid loc -> no because visited can be there too
        #so we have to track used (in a set o(n)) and currspot
        #have to calculate every starting spot 
        #because its strictly increasing, the strictly increasing sequence from a number we can say its 1 + the neighbor.
        #now, we calculate from the neighbor. The neighbor 
        #We can do this easily using 2d storage. If we want o(1) storage, we can also do it
        #we can also 

        #we can use a set to track each index's max, but if its already been used we can just mark it as negative distance that way it makes the array usable too 

        #1) iterate thru every index in the matrix
        #2) we can use recursion and once we calculate, mark as negative
        #3) once we mark it, we know the path length
        #4) if a neighbor is negative, we can do it 
        def calcMaxPath(i,j): 
            if distGrid[i][j] < 0:
                return -1 * distGrid[i][j]
            maxPath = 1
            if i > 0 and grid[i - 1][j] > grid[i][j]:
                maxPath = max(1 + calcMaxPath(i-1, j), maxPath)

            if j > 0 and grid[i][j-1] > grid[i][j]:
                maxPath = max(1 + calcMaxPath(i, j - 1), maxPath)

            if i < len(grid) -1 and grid[i+1][j] > grid[i][j]:
                maxPath = max(1 + calcMaxPath(i + 1, j), maxPath)
            
            if j < len(grid[0]) - 1 and grid[i][j+1] > grid[i][j]:
                maxPath = max(1 + calcMaxPath(i, j+1), maxPath)
            distGrid[i][j] = -1*maxPath
            return maxPath









        maximum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                calcMaxPath(i,j)
                maximum = max(maximum, -1*distGrid[i][j])
        print(matrix)
        return maximum
    

        